#!/bin/bash
for i in *.jpg; do convert -thumbnail 500 $i $i; done;
