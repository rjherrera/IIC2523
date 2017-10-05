for img in "lena" "licht"; do
  for krn in "blur" "double"; do
    for itr in 25 50; do
      for nth in 1 2 4 8 16; do
        NAME=${img}_${krn}_${itr}_${nth}
        COMMAND="./filter $img.png $krn.txt $NAME.png $itr $nth"
        echo "\n$COMMAND:"
        time ./filter assets/inputs/$img.png assets/kernels/$krn.txt assets/outputs/$NAME.png $itr $nth
      done
    done
  done
done