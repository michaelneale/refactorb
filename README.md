# RefactorB

The B stands for bargain!

Have GITHUB_ACCESS_TOKEN and OPENAI_API_KEY handy (the former is needed just for rate limits, you can skip it if you like).

# Usage: 

```shell
python main.py <repository_name> <version_hash> <directory>
```

# Example:

```shell
python main.py TBD54566975/tbdex-pfi-exemplar 519d44ae176d0c6c2b1f1390b8df5fbc05dc8b0c ../pinpayments-pfi/src/
```

This will look at the delta on the repo beteween the current version and the specified hash, and use that as inspiration for how it should change all the code that it finds in the path you give it. 

Good luck!
