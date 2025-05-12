def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
    else:
        hanoi(n - 1, source, destination, auxiliary)
        print(f"Move disk {n} from {source} to {destination}")
        hanoi(n - 1, auxiliary, source, destination)

hanoi(3, 'Source', 'Auxiliary', 'Destination')

