from functools import wraps
import logging
import time


def time_slow(*setting_args, **setting_kwargs):
    if 'threshold' in setting_kwargs:
        threshold = setting_kwargs['threshold']
    else:
        threshold = 0

    def decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            ex_time = time.time() - start
            msg = 'Function {} with arguments {} {} took {}s to execute'\
                .format(func, args, kwargs, ex_time)
            if threshold is not 0 and ex_time > threshold:
                logging.warning(msg)
            else:
                logging.info(msg)
            return result

        return func_wrapper

    # TODO: how to make the difference between @time_slow and @time_slow(func)?
    if len(setting_args) == 1 and not setting_kwargs and \
       callable(setting_args[0]):
        return decorator(setting_args[0])

    return decorator
