from .middleware import TimedService, timed


class ServerTimingSilkMiddleware:
    """
    This middleware will measure the response time for each request,
    and also the time taken for sql queries, if silk is enabled.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def _get_query_timing(self, request):
        try:
            from silk.collector import DataCollector
            from silk.profiling.profiler import silk_meta_profiler
        except ModuleNotFoundError:
            return
        if not hasattr(request, "silk_is_intercepted"):
            return
        with silk_meta_profiler():
            collector = DataCollector()
            silk_request = collector.request
            if silk_request:
                TimedService(
                    name="sql",
                    description="DB Queries",
                    duration=sum([s.time_taken for s in silk_request.queries.all()]),
                )

    def __call__(self, request):
        with timed("request-response", "Request Response"):
            response = self.get_response(request)
        self._get_query_timing(request)
        return response


class ServerTimingSilkViewOnlyMiddleware:
    """
    This middleware would be put as the last middleware, to measure the
    response time of only the underlying view.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        with timed("request-view", "Request View"):
            response = self.get_response(request)
        return response
