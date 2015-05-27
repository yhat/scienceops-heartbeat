from yhat import Yhat, YhatModel, preprocess
import os

class HelloWorld(YhatModel):
    @preprocess(in_type=dict, out_type=dict)
    def execute(self, data):
        me = data['name']
        greeting = "Hello %s!" % me
        return { "greeting": greeting }

yh = Yhat(os.environ["YHAT_USERNAME"], os.environ["YHAT_APIKEY"], "http://sandbox.yhathq.com/")
print(yh.deploy("HelloWorld", HelloWorld, globals(), True))