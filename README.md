# mdtest formatter
A python2/3 simple script to convert [mdtest](https://github.com/hpc/ior) output into CSV format.

## Example
`mdtest -d /tmp/mdtest.test -i3 -I 100 | python2 mdtest_formatter.py`

```
Operation,Max,Min,Mean,Std Dev
Directory creation,673409.75,591355.561,641233.491,35760.634
Directory stat,1181669.923,1042665.9,1108168.788,57029.282
Directory removal,784953.998,764947.066,774565.748,8185.903
File creation,414370.36,405756.883,409122.662,3759.806
File stat,1154467.805,1059613.86,1110038.577,38955.335
File read,648925.046,576751.159,613483.908,29479.017
File removal,748116.615,701611.605,718830.65,20814.849
Tree creation,591365.471,462320.783,521383.535,53245.058
Tree removal,651042.384,461042.094,534898.483,83131.233
```
