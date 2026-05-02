import wandb
print("wandb version:", wandb.__version__)
print("wandb file   :", wandb.__file__)
wandb.login()


run = wandb.init(
    project="deep-learning-cnn-assignment",
    name="wandb_script_test",
    mode="offline"
)

wandb.log({"test_metric": 1.0})
wandb.finish()

print("done")