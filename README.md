# RefactorB

The B stands for bargain!


# Usage: 

```shell
python script.py <repository_name> <version_hash> <directory>
```

# Example:

```shell
python main.py TBD54566975/tbdex-pfi-exemplar 519d44ae176d0c6c2b1f1390b8df5fbc05dc8b0c ../pinpayments-pfi/src/
```

This will look at the delta on the repo beteween the current version and the specified hash, and use that as inspiration for how it should change all the code that it finds in the path you give it. 

Good luck!