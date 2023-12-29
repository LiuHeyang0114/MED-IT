#!/usr/bin/env bash

    if [ ${stage} -le 6 ] && [ ${stop_stage} -ge 6 ]; then
        if [ "${token_type}" = bpe ]; then
              cat /GPFS/data/heyangliu/BrainGPT_data/derived/transcriptions/train.txt | while read line
              do
                  echo " ${line}" | spm_encode --model=/GPFS/data/heyangliu/BrainGPT_data/BPE/brain.model --output_format=id >> /GPFS/data/heyangliu/BrainGPT_data/derived/transcriptions/train_bpe.txt
              done

              cat /GPFS/data/heyangliu/BrainGPT_data/derived/transcriptions/dev.txt | while read line
              do
                  echo " ${line}" | spm_encode --model=/GPFS/data/heyangliu/BrainGPT_data/BPE/brain.model --output_format=id >> /GPFS/data/heyangliu/BrainGPT_data/derived/transcriptions/dev_bpe.txt
              done
        fi
    fi