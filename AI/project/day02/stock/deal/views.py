from django.shortcuts import render
from userinfo.models import *
from stocks.models import *
from .models import *
from django.contrib.auth.hashers import check_password
from django.db.models import F
import json
import datetime
import decimal
# Create your views here.
def deal(user, sob, stockNo, amount, price, tradepwd, price_range):
    result = {}
    if sob == "buy":
        # try
        fund = Fund.objects.get(user=user)
        money = fund.money - decimal.Decimal(amount)*decimal.Decimal(price)
        stock = Stock.objects.get(stonumber=stockNo)
        datetimes = datetime.datetime.now()
        if money >= 0:
            fund.frozen_money = fund.frozen_money + decimal.Decimal(amount)*decimal.Decimal(price)
            fund.save()
            range = (decimal.Decimal(price)-decimal.Decimal(price_range),decimal.Decimal(price))
            sale_stock = BOSStock.objects.filter(stock__stonumber=stockNo, role=1, price__range=range)
            if len(sale_stock)<=0:
                bosstock = BOSStock()
                bosstock.user = user
                bosstock.stock = stock
                bosstock.role = 0
                bosstock.price = decimal.Decimal(price)
                bosstock.amount = decimal.Decimal(amount)
                bosstock.datetime = datetimes
                bosstock.save()
                result['msg'] = "无卖家，买家已挂单"
                return result
            else:
                for st in sale_stock:
                    if int(amount) > st.amount:
                        hold = Hold.objects.filter(user=user, stock=stock)
                        if len(hold) > 0:
                            hold.update(amount=F('amount') + st.amount)
                        else:
                            Hold.objects.create(user=user, stock=stock, amount=st.amount, frozen=0)
                        bfund = Fund.objects.get(user=user)
                        bfund.money = bfund.money - st.amount*st.price
                        bfund.frozen_money = bfund.frozen_money - st.amount*st.price
                        bfund.save()
                        sfund =Fund.objects.get(user=st.user)
                        sfund.money = sfund.money + st.amount*st.price
                        sfund.save()
                        Hold.objects.filter(user=st.user, stock=stock).update(amount=F('amount') - st.amount)
                        DealStock.objects.create(suser=st.user, buser=user, price=st.price, amount=st.amount, datetime=datetimes, stock=stock)
                        amount = int(amount) - st.amount
                        st.delete()
                    else:
                        hold = Hold.objects.filter(user=user, stock=stock)
                        if len(hold) > 0:
                            hold.update(amount=F('amount') + st.amount)
                        else:
                            Hold.objects.create(user=user, stock=stock, amount=st.amount, frozen=0)
                        bfund = Fund.objects.filter(user=user)
                        bfund.frozen_money = bfund.frozen_money - decimal.Decimal(amount)*decimal.Decimal(price)
                        bfund.money = bfund.money- decimal.Decimal(amount)*decimal.Decimal(price)
                        bfund.save()
                        Hold.objects.filter(user=user).update(amount=F('amount') + st.amount)
                        sfund = Fund.objects.get(user=st.user)
                    sfund.money = sfund.money + decimal.Decimal(amount)*decimal.Decimal(price)
                    sfund.save()
                    DealStock.objects.create(suser=st.user, buser=user, price=st.price, amount=amount,
                                             datetime=datetimes, stock=stock)
                    st.amount = st.amount - decimal.Decimal(amount)
                    st.save()
                if int(amount)>0:
                    bosstock = BOSStock()
                    bosstock.user = user
                    bosstock.stock = stock
                    bosstock.role = 0
                    bosstock.price = decimal.Decimal(price)
                    bosstock.amount = decimal.Decimal(amount)
                    bosstock.datetime = datetimes
                    bosstock.save()
                    result['msg']="剩余股票已挂单"
                    return result

        else:
            result['msg'] = "金额不足"
            return result



    elif sob == "sale":
        pass