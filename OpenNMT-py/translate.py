#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from itertools import repeat

from onmt.utils.logging import init_logger
from onmt.utils.misc import split_corpus
from onmt.translate.translator import build_translator

import onmt.opts as opts
from onmt.utils.parse import ArgumentParser
import os

INPUT_DIR = './input_data/'
def main(opt):
	ArgumentParser.validate_translate_opts(opt)
	logger = init_logger(opt.log_file)
	# editing from here:
	out_dir_list = os.listdir('./testout')
	for file in os.listdir(INPUT_DIR):
		if 'output_'+file in out_dir_list:
			continue
		out_file = open('testout/output_'+file.split('/')[-1],'w')
		opt.src = INPUT_DIR+file
		translator = build_translator(opt, report_score=True,out_file=out_file)
		src_shards = split_corpus(opt.src, opt.shard_size)
		tgt_shards = split_corpus(opt.tgt, opt.shard_size) \
			if opt.tgt is not None else repeat(None)
		shard_pairs = zip(src_shards, tgt_shards)
		for i, (src_shard, tgt_shard) in enumerate(shard_pairs):
			logger.info("Translating shard %d." % i)
			translator.translate(
				src=src_shard,
				tgt=tgt_shard,
				src_dir=opt.src_dir,
				batch_size=opt.batch_size,
				attn_debug=opt.attn_debug
				)
		out_file.close()

def _get_parser():
	parser = ArgumentParser(description='translate.py')

	opts.config_opts(parser)
	opts.translate_opts(parser)
	return parser


if __name__ == "__main__":
	parser = _get_parser()

	opt = parser.parse_args()
	main(opt)
