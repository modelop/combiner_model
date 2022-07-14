## Combiner Example Model

This is a simple framework for how you can combine multiple input slots together into a single processing stream
for use by a model.  The action function will wait until it has a complete set of records from all streams (in this
case three), and then will call the run_model_on_record() function with a record from each stream in the order received.

You should place your model scoring code inside of the run_model_on_record() function and have it return your scoring
result in a dictionary format.  This will then be output on the single output stream defined.

This code is necessary as depending upon the input stream types, records could come in faster or slower from each of the
different streams and arrive out of order.  So for instance record 0 on stream 0 and record 1 on stream 0 could both
arrive before record 0 on stream one.  So to handle this we simply place each record into a queue and will only process
a full combined record once we receive a record on all defined input streams.

The main function can be updated to have records compatible with your model and can be used for testing the
model out by running the main function locally, and does not require deploying to the modelop engine to run.  Complete a
successful run of that locally, and then deploy the finished model to a modelop engine, create a snapshot, and run a
simple batch scoring job with the multiple input streams.