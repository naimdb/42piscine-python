import os


def ft_tqdm(lst: range):
    total = len(lst)
    terminal_width = os.get_terminal_size().columns
    info_length = len(f"100%|| {total}/{total}")
    bar_width = terminal_width - info_length

    for i, item in enumerate(lst, 1):
        percent = (i / total) * 100
        filled_length = int(bar_width * i / total)

        bar = '█' * filled_length + ' ' * (bar_width - filled_length)

        print(f"\r{percent:3.0f}%|{bar}| {i}/{total}", end="", flush=True)
        yield item
