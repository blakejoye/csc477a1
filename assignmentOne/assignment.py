import matplotlib.pyplot as plt

def plot_waveform(signal, title, ax):
    x_values = list(range(len(signal))) + [len(signal)]
    ax.step(x_values, signal + [signal[-1]], where='post')
    ax.set_ylim(-0.5, 1.5)
    ax.set_title(title)
    ax.set_ylabel('Amplitude')
    ax.set_xlabel('Time (unit intervals)')
    ax.set_yticks([0, 1])
    ax.grid(True)

def nrz_encoding(bits):
    return [int(b) for b in bits]

def manchester_encoding(bits):
    return [0 if b == '1' else 1 if i % 2 == 0 else 1 if b == '0' else 0 for i, b in enumerate(bits + bits[-1]) for _ in (0, 1)]

def differential_manchester_encoding(bits):
    output = [1]
    for i, bit in enumerate(bits):
        if bit == '0':
            output.append(output[-1])
        else:
            output.append(1 - output[-1])
        output.append(output[-1])
    return output[1:]

def apply_clock_skew(signal, skew_ratio):
    """Apply clock skew to a signal. Each level in the signal is held for `skew_ratio` times longer."""
    skewed_signal = []
    for value in signal:
        skewed_signal.extend([value] * skew_ratio)
    return skewed_signal

def generate_waveforms(binary_sequence, skew_ratio=1):
    fig, axs = plt.subplots(3, 1, figsize=(10, 6), tight_layout=True)

    # NRZ encoding
    nrz_signal = nrz_encoding(binary_sequence)
    nrz_skewed = apply_clock_skew(nrz_signal, skew_ratio)
    plot_waveform(nrz_skewed, f'NRZ Encoding (Skew {skew_ratio}x)', axs[0])

    # Manchester encoding
    manchester_signal = manchester_encoding(binary_sequence)
    manchester_skewed = apply_clock_skew(manchester_signal, skew_ratio)
    plot_waveform(manchester_skewed, f'Manchester Encoding (Skew {skew_ratio}x)', axs[1])

    # Differential Manchester encoding
    diff_manchester_signal = differential_manchester_encoding(binary_sequence)
    diff_manchester_skewed = apply_clock_skew(diff_manchester_signal, skew_ratio)
    plot_waveform(diff_manchester_skewed, f'Differential Manchester Encoding (Skew {skew_ratio}x)', axs[2])

    plt.show()

def main():
    binary_sequence = input("Please enter a binary sequence: ")
    skew_ratio = int(input("Enter skew ratio (1 for no skew, 2 for double duration, etc.): "))
    if not all(c in '01' for c in binary_sequence):
        print("Invalid input! Only binary digits (0 or 1) are allowed.")
    else:
        generate_waveforms(binary_sequence, skew_ratio)

if __name__ == '__main__':
    main()
