fs = require('fs');

function wordVal(word) {
  code = 0
  for (var i=0; i<word.length; i++){
    code += word.toLowerCase().charCodeAt(i) - 'a'.charCodeAt(0) + 1;
  }
  return code;
}

fs.readFile('./words.txt', function(err, data){
  if (err) {
    console.log('File read error', err);
    return;
  }
  data = "[" + data + "]";
  data = JSON.parse(data);
  count = 0;
  for (var i=0; i<data.length; i++){
    var val = wordVal(data[i]);
    var test = Math.sqrt(1 + (8*val));
    if (Number.isInteger(test) && test > 1) {
      console.log('Passed: ', data[i], " Val: ", val, " Test: ", test);
      count += 1;
    }
  }
  console.log('SOLUTION: ', count);
});
