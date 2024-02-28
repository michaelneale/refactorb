# RefactorB

Auto update your code to a new version of an API, by pointing it at another repo that has already done that migration. 


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


![image](https://github.com/michaelneale/refactorb/assets/14976/1b8b66e5-7ed2-4490-be2f-99fa0efa7cc0)
