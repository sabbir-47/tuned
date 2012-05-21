import interfaces
import storage

class Factory(interfaces.Factory):
	__slots__ = ["_storage_provider"]

	def __init__(self, storage_provider):
		self._storage_provider = storage_provider

	def create(self, namespace):
		return storage.Storage(self._storage_provider, namespace)
