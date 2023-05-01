import torch


def main():
	checkpoint = torch.load('ckp.pth', map_location=torch.device('cpu'))

	print(checkpoint.keys())
	print(checkpoint['label_emb.weight'])
	print(model_state_dict)
main()
