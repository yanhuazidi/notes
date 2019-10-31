

# 通过threading.Event()可以创建一个事件管理标志，该标志（event）默认为False
# event对象主要有四种方法可以调用：

# event.wait(timeout=None)：调用该方法的线程会被阻塞，如果设置了timeout参数，超时后，线程会停止阻塞继续执行；
                    # 并不会改变 event 状态;
# event.set()：将event的标志设置为True，调用wait()方法的所有线程将被唤醒,继续执行；
# event.clear()：将event的标志设置为False，调用wait()方法的所有线程将被阻塞；
# event.isSet()：判断event的标志是否为True,返回bool。



import threading
from time import sleep
 
def test(n, event):
	while not event.isSet():
		print('Thread %s is ready' % n)
		sleep(1)
	event.wait()
	while event.isSet():
		print('Thread %s is running' % n)
		sleep(1)
 
def main():
	event = threading.Event()
	for i in range(2):
		th = threading.Thread(target=test, args=(i, event))
		th.start()
	sleep(3)
	print('----- event is set -----')
	event.set()
	sleep(3)
	print('----- event is clear -----')
	event.clear()
 
if __name__ == '__main__':
	main()

# Thread 0 is ready
# Thread 1 is ready
# Thread 0 is ready
# Thread 1 is ready
# Thread 0 is ready
# Thread 1 is ready
# ----- event is set -----
# Thread 0 is running
# Thread 1 is running
# Thread 0 is running
# Thread 1 is running
# Thread 0 is running
# Thread 1 is running
# ----- event is clear -----

