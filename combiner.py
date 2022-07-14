# modelop.slot.0: in-use
# modelop.slot.1: in-use
# modelop.slot.2: in-use
# modelop.slot.4: in-use

import json

RECORD = [[], [], []]


#
# Put your model code in here.  This is a full record from all three input slots and you can now process it with
# your specific model code
#
def run_model_on_record(record):
    return record


# modelop.score
def action(data, slot_number):
    global RECORD

    RECORD[int(slot_number / 2)].append(data)

    if not RECORD[0] or not RECORD[1] or not RECORD[2]:
        return
    else:
        record_to_process = RECORD[0].pop(0)
        record_to_process.update(RECORD[1].pop(0))
        record_to_process.update(RECORD[2].pop(0))
        yield run_model_on_record(record_to_process)


#
# This is where you can do some simple testing of the action function to make sure your model is behaving
# as it should. Just manually add in your example dictionary based records in here and you can validate the output
# of your model without having to run on the engine
#
def main():
    if next(action({"foo": 1}, 0)) is not None:
        print("Error received value back on first slot")

    if next(action({"bar": "Strvalue"}, 2)) is not None:
        print("Error received value back on second slot")

    print(json.dumps(next(action({"objectValue": {"foo" : 1, "bar": False}}, 4)), indent=4))

    if next(action({"foo": 1}, 0)) is not None:
        print("Error received value back on first slot")

    if next(action({"bar" : "This value should not be present"}, 0)) is not None:
        print("Error received value back on first slot")

    if next(action({"bar": "Strvalue"}, 2)) is not None:
        print("Error received value back on second slot")

    print(json.dumps(next(action({"objectValue": {"foo" : 1, "bar": False}}, 4)), indent=4))


if __name__ == '__main__':
    main()
