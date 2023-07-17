import torch

loss_metric_dict = {
    "MSE" : torch.nn.MSELoss(reduction = "mean")
}

def loss_metric(loss_metric_string):
    """
    Returns the loss metric module.
    """
    if loss_metric_string in loss_metric_dict:
        return loss_metric_dict[loss_metric_string]
    else:
        raise ValueError("Invalid loss metric")
