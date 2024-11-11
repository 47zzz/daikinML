import torch
from torch.utils.data import DataLoader, Dataset

class SimpleDataset(Dataset):
    def __len__(self):
        return 100

    def __getitem__(self, idx):
        return idx

if __name__ == "__main__":
    import torch.multiprocessing as mp
    mp.set_start_method('spawn', force=True)  # 確認在 Windows 上使用這個設定

    dataset = SimpleDataset()
    loader = DataLoader(dataset, batch_size=10, num_workers=2)
    
    for batch in loader:
        print(batch)
