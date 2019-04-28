import time, datetime, sys

class pBAR():
    def __init__(self, maxval=100):
        self.maxval = maxval
        self.start_time = None
        self.last_time = None
        self.finished = False

    def start(self):
        self.start_time = time.time()
        self.last_time = self.start_time

    def update(self, value, dict_data=None):
        block = int(round(value))
        percentage = block/self.maxval
        
        cur_time = time.time()
        dur_time = cur_time - self.start_time
        self.last_time = cur_time
        eta = dur_time*(self.maxval-block)/block

        if dur_time < 0.01:
            ETA = '-:--:--'
        else:
            ETA = str(datetime.timedelta(seconds=int(eta)))[:7]

        if dict_data is not None:
            extra_data = ''
            for elem in dict_data:
                extra_data = extra_data + '{}:{}, '.format(elem, dict_data[elem])
            extra_data = extra_data[:-2]
            text = "\r{:.0%}:[{}] ETA: {}, {}".format(percentage, "#"*block + "-"*(self.maxval-block), ETA, extra_data)
        else:
            text = "\r{:.0%}:[{}] ETA: {}".format(percentage, "#"*block + "-"*(self.maxval-block), ETA)
        sys.stdout.write(text)
        sys.stdout.flush()
    
    def finish(self):
        self.finished = True
        sys.stdout.write('\n')

if __name__ == '__main__':
    pbar = pBAR()
    pbar.start()
    for i in range(100):
        pbar.update(i+1)

    pbar.finish()
