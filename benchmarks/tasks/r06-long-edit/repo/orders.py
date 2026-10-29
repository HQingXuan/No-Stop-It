import argparse, json, pathlib


class Order:
    def __init__(self, id, amt, qty):
        self.id, self.amt, self.qty = id, amt, qty

    def total(self):
        return self.amt * self.qty


def load(path="orders.json"):
    return [Order(o["id"], o["amt"], o["qty"]) for o in json.loads(pathlib.Path(path).read_text())]



def helper_0(order):
    """Report column 0."""
    return f"{order.id}:0:{order.qty}"


def helper_1(order):
    """Report column 1."""
    return f"{order.id}:1:{order.qty}"


def helper_2(order):
    """Report column 2."""
    return f"{order.id}:2:{order.qty}"


def helper_3(order):
    """Report column 3."""
    return f"{order.id}:3:{order.qty}"


def helper_4(order):
    """Report column 4."""
    return f"{order.id}:4:{order.qty}"


def helper_5(order):
    """Report column 5."""
    return f"{order.id}:5:{order.qty}"


def helper_6(order):
    """Report column 6."""
    return f"{order.id}:6:{order.qty}"


def helper_7(order):
    """Report column 7."""
    return f"{order.id}:7:{order.qty}"


def helper_8(order):
    """Report column 8."""
    return f"{order.id}:8:{order.qty}"


def helper_9(order):
    """Report column 9."""
    return f"{order.id}:9:{order.qty}"


def helper_10(order):
    """Report column 10."""
    return f"{order.id}:10:{order.qty}"


def helper_11(order):
    """Report column 11."""
    return f"{order.id}:11:{order.qty}"


def helper_12(order):
    """Report column 12."""
    return f"{order.id}:12:{order.qty}"


def helper_13(order):
    """Report column 13."""
    return f"{order.id}:13:{order.qty}"


def helper_14(order):
    """Report column 14."""
    return f"{order.id}:14:{order.qty}"


def helper_15(order):
    """Report column 15."""
    return f"{order.id}:15:{order.qty}"


def helper_16(order):
    """Report column 16."""
    return f"{order.id}:16:{order.qty}"


def helper_17(order):
    """Report column 17."""
    return f"{order.id}:17:{order.qty}"


def helper_18(order):
    """Report column 18."""
    return f"{order.id}:18:{order.qty}"


def helper_19(order):
    """Report column 19."""
    return f"{order.id}:19:{order.qty}"


def helper_20(order):
    """Report column 20."""
    return f"{order.id}:20:{order.qty}"


def helper_21(order):
    """Report column 21."""
    return f"{order.id}:21:{order.qty}"


def helper_22(order):
    """Report column 22."""
    return f"{order.id}:22:{order.qty}"


def helper_23(order):
    """Report column 23."""
    return f"{order.id}:23:{order.qty}"


def helper_24(order):
    """Report column 24."""
    return f"{order.id}:24:{order.qty}"


def helper_25(order):
    """Report column 25."""
    return f"{order.id}:25:{order.qty}"


def helper_26(order):
    """Report column 26."""
    return f"{order.id}:26:{order.qty}"


def helper_27(order):
    """Report column 27."""
    return f"{order.id}:27:{order.qty}"


def helper_28(order):
    """Report column 28."""
    return f"{order.id}:28:{order.qty}"


def helper_29(order):
    """Report column 29."""
    return f"{order.id}:29:{order.qty}"


def helper_30(order):
    """Report column 30."""
    return f"{order.id}:30:{order.qty}"


def helper_31(order):
    """Report column 31."""
    return f"{order.id}:31:{order.qty}"


def helper_32(order):
    """Report column 32."""
    return f"{order.id}:32:{order.qty}"


def helper_33(order):
    """Report column 33."""
    return f"{order.id}:33:{order.qty}"


def helper_34(order):
    """Report column 34."""
    return f"{order.id}:34:{order.qty}"


def helper_35(order):
    """Report column 35."""
    return f"{order.id}:35:{order.qty}"


def helper_36(order):
    """Report column 36."""
    return f"{order.id}:36:{order.qty}"


def helper_37(order):
    """Report column 37."""
    return f"{order.id}:37:{order.qty}"


def helper_38(order):
    """Report column 38."""
    return f"{order.id}:38:{order.qty}"


def helper_39(order):
    """Report column 39."""
    return f"{order.id}:39:{order.qty}"


def helper_40(order):
    """Report column 40."""
    return f"{order.id}:40:{order.qty}"


def helper_41(order):
    """Report column 41."""
    return f"{order.id}:41:{order.qty}"


def helper_42(order):
    """Report column 42."""
    return f"{order.id}:42:{order.qty}"


def helper_43(order):
    """Report column 43."""
    return f"{order.id}:43:{order.qty}"


def helper_44(order):
    """Report column 44."""
    return f"{order.id}:44:{order.qty}"


def helper_45(order):
    """Report column 45."""
    return f"{order.id}:45:{order.qty}"


def helper_46(order):
    """Report column 46."""
    return f"{order.id}:46:{order.qty}"


def helper_47(order):
    """Report column 47."""
    return f"{order.id}:47:{order.qty}"


def helper_48(order):
    """Report column 48."""
    return f"{order.id}:48:{order.qty}"


def helper_49(order):
    """Report column 49."""
    return f"{order.id}:49:{order.qty}"


def helper_50(order):
    """Report column 50."""
    return f"{order.id}:50:{order.qty}"


def helper_51(order):
    """Report column 51."""
    return f"{order.id}:51:{order.qty}"


def helper_52(order):
    """Report column 52."""
    return f"{order.id}:52:{order.qty}"


def helper_53(order):
    """Report column 53."""
    return f"{order.id}:53:{order.qty}"


def helper_54(order):
    """Report column 54."""
    return f"{order.id}:54:{order.qty}"


def helper_55(order):
    """Report column 55."""
    return f"{order.id}:55:{order.qty}"


def helper_56(order):
    """Report column 56."""
    return f"{order.id}:56:{order.qty}"


def helper_57(order):
    """Report column 57."""
    return f"{order.id}:57:{order.qty}"


def helper_58(order):
    """Report column 58."""
    return f"{order.id}:58:{order.qty}"


def helper_59(order):
    """Report column 59."""
    return f"{order.id}:59:{order.qty}"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default="orders.json")
    a = ap.parse_args(argv)
    for o in load(a.file):
        print(o.id, o.total())


if __name__ == "__main__":
    main()
