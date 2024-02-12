import logging
import keras
logging.warning("[OVERRIDE]")
# print("[OVERRIDE]")

# # temp = keras.layers.core.dense.Dense.__call__
# temp = keras.layers.core.dense.Dense.call
# def MyDense(*args, **kwargs):
#     # logging.warning("[OVERRIDE] MyDense")
#     print("MyDense", args, kwargs)
#     return temp(*args, **kwargs)
# # keras.layers.core.dense.Dense.__call__ = MyDense
# keras.layers.core.dense.Dense.call = MyDense


temp = keras.engine.base_layer.Layer.__call__
def MyLayer(*args, **kwargs):
    print("[OVERRIDE] MyLayer")
    return temp(*args, **kwargs)
keras.engine.base_layer.Layer.__call__ = MyLayer


# temp = keras.engine.base_layer.Layer.call
# def MyLayer(inputs, *args, **kwargs):
#     print("[OVERRIDE] MyLayer")
#     return temp(inputs, *args, **kwargs)
# keras.engine.base_layer.Layer.call