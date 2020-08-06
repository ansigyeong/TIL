const array = [1, 2, 3, 4];

for(let i = 0; i < array.length; i++) // index read/write, break ok
  console.log('basic ' + array[i]);

for(const i in array)               // index read, break ok
  console.log('in ' + array[i]);

for(const v of array)               // break ok
  console.log('of ' + v);

array.some(v => {                   // break ok
  console.log('some ' + v);
  return (v == 3)
});

array.forEach(v => console.log('each ' + v));   // break x
