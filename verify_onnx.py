import onnxruntime
import os
capi_dir = os.path.join(os.path.dirname(onnxruntime.__file__), 'capi')
print(capi_dir)
print(os.listdir(capi_dir))  # Should list files like onnxruntime.dll, _onnxruntime_pybind11_state.pyd, etc.