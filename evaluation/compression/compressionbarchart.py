import numpy as np
import matplotlib.pyplot as plt


labels = ['raw\nPacket','trimmed\npayload','ip 5 tuple','compressed']

timestamps = np.array([16,16,16,8])
ipHeader = [20,20,5,0]
meanHeader = [18.16,18.16,3,0]
payloads = [316.37,0,0,0]
compressed = [0,0,0,9.2542]

width = 0.35
fig, ax = plt.subplots()


ax.bar(labels, timestamps, width, label='timestamp')
ax.bar(labels, ipHeader, width, label='ip header', bottom=timestamps)
ax.bar(labels, meanHeader, width, label='mean header' , bottom=[x + y for x, y in zip(timestamps, ipHeader)])
ax.bar(labels, payloads, width, label='payload' , bottom=[x + y + z for x, y, z in zip(timestamps, ipHeader, meanHeader)])
ax.bar(labels, compressed, width, label='compressed' , bottom=[w + x + y + z for w, x, y, z in zip(timestamps, ipHeader, meanHeader, payloads)])
ax.legend()

ax.set_ylabel('bytes')

ax.set_title('Compression rate')

#ax.set_yscale("symlog")

plt.savefig('compression_rate_payload.png')


fig, ax = plt.subplots()

labels = ['trimmed\npayload','ip 5 tuple','compressed']

timestamps = [16,16,8]
ipHeader = [20,5,0]
meanHeader = [18.16,3,0]
payloads = [0,0,0]
compressed = [0,0,9.2542]

width = 0.35


ax.bar(labels, timestamps, width, label='timestamp')
ax.bar(labels, ipHeader, width, label='ip header', bottom=timestamps)
ax.bar(labels, meanHeader, width, label='mean header' , bottom=[x + y for x, y in zip(timestamps, ipHeader)])
ax.bar(labels, payloads, width, label='payload' , bottom=[x + y + z for x, y, z in zip(timestamps, ipHeader, meanHeader)])
ax.bar(labels, compressed, width, label='compressed' , bottom=[w + x + y + z for w, x, y, z in zip(timestamps, ipHeader, meanHeader, payloads)])
ax.legend()

ax.set_ylabel('bytes')

ax.set_title('Compression rate')

plt.savefig('compression_rate.png')

