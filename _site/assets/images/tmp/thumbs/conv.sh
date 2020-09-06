#!/bin/bash
for i in *.jpg; do convert -thumbnail 600 $i $i; done;
