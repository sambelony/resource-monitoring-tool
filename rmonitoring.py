import pandas as pd
import psutil
import time
import datetime
import argparse
import subprocess
import platform
from datetime import datetime
from matplotlib import pyplot as plt
import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')


class Monitoring:

    def __init__(self, file_path):
        """Running process (self.process) -> getting PID of process (self.pid) and passes it to psutil.Process"""
        self.process = subprocess.Popen(file_path)
        self.pid = self.process.pid
        logging.info(f"Process {file_path} started. PID {self.pid}")
        self.py = psutil.Process(self.pid)

    def run_monitoring(self, interval_time):
        """Monitoring process params while it's running and writing collected data to .csv file."""
        try:
            with open(f'{os.path.basename(process).split(".")[0]}.csv', 'w') as file:
                if platform.system() == 'Windows':
                    logging.info("Found Windows platform")
                    file.write(f'Date; CPU; Working Set; Private Bytes; Number of handles\n')
                    while True:
                        self.process.poll()
                        if self.process.returncode is None:
                            w_set = self.py.memory_info()[0]
                            p_bytes = self.py.memory_info()[-1]
                            num_handles = self.py.num_handles()
                            cpu_use = self.py.cpu_percent()
                            logging.info("Data collected")
                            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            file.write(f'{date}; {cpu_use}; {w_set}; {p_bytes}; {num_handles} \n')
                            logging.info("Data submitted")
                        else:
                            break
                        time.sleep(interval_time)
                elif platform.system() == 'Linux':
                    logging.info("Found Windows platform")
                    file.write(f'Date; CPU; Resident Set Size; Virtual Memory Size; File Descriptors\n')
                    while True:
                        self.process.poll()
                        if self.process.returncode is None:
                            f_descriptors = self.py.num_fds()
                            rss = self.py.memory_info()[0]
                            vms = self.py.memory_info()[1]
                            cpu_use = self.py.cpu_percent()
                            logging.info("Data submitted")
                            unix_date = time.time()
                            reg_date = datetime.datetime.fromtimestamp(unix_date).strftime("%Y-%m-%d %H:%M:%S")
                            file.write(f'{reg_date}; {cpu_use}; {rss}; {vms}; {f_descriptors} \n')
                            logging.info("Data submitted")
                        else:
                            break
                        time.sleep(interval_time)
                else:
                    logging.error('Linux/Windows not found!')
        except psutil.NoSuchProcess:
            logging.error('Process closed, tracking stopped!')
        finally:
            self.process.kill()



    @staticmethod
    def make_graph(filename):
        if platform.system() == 'Windows':
            headers = ['Date', 'CPU', 'Working Set', 'Private Bytes', 'Number of handles']
        else:
            headers = ['Date', 'CPU', 'Resident Set Size', 'Virtual Memory Size', 'File Descriptors']
        df = pd.read_csv(filename, skiprows=1, names=headers, sep=';')
        for data in headers[1:]:
            x = df['Date']
            y = df[data]
            plt.title(f'{data} graph')
            plt.xlabel('Date')
            plt.ylabel(data)
            plt.xticks(ticks=range(len(y)), labels=x, rotation=90)
            plt.subplots_adjust(bottom=0.4)
            plt.plot(x, y, label=data)
            plt.savefig(f'{os.path.basename(process).split(".")[0]} {data}.png', dpi=300)
            plt.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--process',
        help='Enter process name with extension / full path',
        type=str,
        default='Notepad.exe'
    )
    parser.add_argument(
        '--interval',
        help='Enter an interval in seconds',
        type=int,
        default=5,
    )
    parser.add_argument(
        '--graph',
        help='Save graphs? Enter Y or N',
        type=str,
        default='n',
    )
    args = parser.parse_args()
    interval = args.interval
    process = args.process
    graph = args.graph

    monitoring = Monitoring(process)
    monitoring.run_monitoring(interval)

    if graph == 'y':
        monitoring.make_graph(f'{os.path.basename(process).split(".")[0]}.csv')