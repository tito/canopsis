import unittest

from pyperfstore3.manager import Manager, DEFAULT_PERIOD
from pyperfstore3.timewindow import TimeWindow, get_offset_timewindow


class ManagerTest(unittest.TestCase):

	def setUp(self):
		self.manager = Manager()

	def test_put_get_data(self):

		timewindow = TimeWindow()

		data_id = 'test_manager'

		self.manager.remove(data_id=data_id, with_meta=True)

		count = self.manager.count(data_id=data_id)
		self.assertEqual(count, 0)

		tv0 = (int(timewindow.start()), None)
		tv1 = (int(timewindow.start() + 1), 0)
		tv2 = (int(timewindow.stop()), 2)
		tv3 = (int(timewindow.stop() + 1000000), 3)

		# set values with timestamp without order
		points = [tv0, tv2, tv1, tv3]

		meta = {'plop': None}

		period = DEFAULT_PERIOD

		self.manager.put(
			data_id=data_id,
			points_or_point=points,
			meta=meta,
			period=period)

		data, _meta = self.manager.get(
			data_id=data_id,
			timewindow=timewindow,
			period=period,
			with_meta=True)

		self.assertEqual(meta, _meta[0][1])

		self.assertEqual([tv0, tv1, tv2], data)

		# remove 1 data at stop point
		_timewindow = get_offset_timewindow(timewindow.stop())

		self.manager.remove(
			data_id=data_id,
			timewindow=_timewindow,
			period=period)

		data, _meta = self.manager.get(
			data_id=data_id,
			timewindow=timewindow,
			period=period,
			with_meta=True)

		self.assertEqual(meta, _meta[0][1])

		self.assertEqual(data, [tv0, tv1])

		# get data on timewindow
		data, _meta = self.manager.get(
			data_id=data_id,
			timewindow=timewindow,
			period=period,
			with_meta=True)

		self.assertEqual(meta, _meta[0][1])

		# get all data
		data, _meta = self.manager.get(
			data_id=data_id,
			period=period,
			with_meta=True)

		self.assertEqual(meta, _meta[0][1])

		self.assertEqual(len(data), 3)

		# remove all data
		self.manager.remove(
			data_id=data_id,
			with_meta=True)

		data, _meta = self.manager.get(
			data_id=data_id,
			period=period,
			with_meta=True)

		self.assertEqual(len(_meta), 0)

		self.assertEqual(len(data), 0)

if __name__ == '__main__':
	unittest.main()