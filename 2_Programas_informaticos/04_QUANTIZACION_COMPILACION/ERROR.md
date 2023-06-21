# Error
<pre>
File "/opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/python3.6/site-packages/python_utils/converters.py", line 89

    if match := regexp.search(input_):
              ^
SyntaxError: invalid syntax
</pre>
sol: cambiar esa linea del archivo del container (Utilizando el atach de visual code ) por 
<pre>
match = regexp.search(input_)
if match :

</pre>