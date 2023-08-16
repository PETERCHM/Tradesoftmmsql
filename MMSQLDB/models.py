# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accessrightstbl(models.Model):
    autonum = models.CharField(db_column='AutoNum', primary_key=True, max_length=200)  # Field name made lowercase.
    usertitle = models.CharField(db_column='UserTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    billing = models.CharField(db_column='Billing', max_length=200, blank=True, null=True)  # Field name made lowercase.
    splitbills = models.CharField(db_column='SplitBills', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mergebills = models.CharField(db_column='MergeBills', max_length=200, blank=True, null=True)  # Field name made lowercase.
    billchanges = models.CharField(db_column='BillChanges', max_length=200, blank=True, null=True)  # Field name made lowercase.
    adddelitems = models.CharField(db_column='AddDelItems', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemchanges = models.CharField(db_column='ItemChanges', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stocktaking = models.CharField(db_column='StockTaking', max_length=200, blank=True, null=True)  # Field name made lowercase.
    purchases = models.CharField(db_column='Purchases', max_length=200, blank=True, null=True)  # Field name made lowercase.
    breakages = models.CharField(db_column='Breakages', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stockreports = models.CharField(db_column='StockReports', max_length=200, blank=True, null=True)  # Field name made lowercase.
    questionbills = models.CharField(db_column='QuestionBills', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cashiersum = models.CharField(db_column='CashierSum', max_length=200, blank=True, null=True)  # Field name made lowercase.
    endshift = models.CharField(db_column='EndShift', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftbackups = models.CharField(db_column='ShiftBackups', max_length=200, blank=True, null=True)  # Field name made lowercase.
    monthlyrpts = models.CharField(db_column='MonthlyRpts', max_length=200, blank=True, null=True)  # Field name made lowercase.
    translog = models.CharField(db_column='TransLog', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accessrights = models.CharField(db_column='AccessRights', max_length=200, blank=True, null=True)  # Field name made lowercase.
    recptmsg = models.CharField(db_column='RecptMsg', max_length=200, blank=True, null=True)  # Field name made lowercase.
    waiters = models.CharField(db_column='Waiters', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginusers = models.CharField(db_column='LoginUsers', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accessrightstbl'


class Accompanimentstbl(models.Model):
    auto = models.IntegerField(db_column='Auto', blank=True, null=True)  # Field name made lowercase.
    accom1 = models.CharField(db_column='Accom1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accom2 = models.CharField(db_column='Accom2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accom3 = models.CharField(db_column='Accom3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accom4 = models.CharField(db_column='Accom4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accom5 = models.CharField(db_column='Accom5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accompanimentstbl'


class Adddata(models.Model):
    added_id = models.AutoField(db_column='added_ID', primary_key=True)  # Field name made lowercase.
    added_bno = models.IntegerField(db_column='added_BNo', blank=True, null=True)  # Field name made lowercase.
    added_oid = models.IntegerField(db_column='added_OID', blank=True, null=True)  # Field name made lowercase.
    added_icode = models.IntegerField(db_column='added_iCode', blank=True, null=True)  # Field name made lowercase.
    added_from = models.CharField(db_column='added_From', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemdesc = models.CharField(db_column='itemDesc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    added_qty = models.FloatField(db_column='added_Qty', blank=True, null=True)  # Field name made lowercase.
    added_when = models.DateField(db_column='added_When', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adddata'


class BbkTillmaster(models.Model):
    transno = models.AutoField(db_column='TransNo', primary_key=True)  # Field name made lowercase.
    tillpcname = models.CharField(db_column='TillPcName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tilltellerid = models.IntegerField(db_column='TillTellerID', blank=True, null=True)  # Field name made lowercase.
    tilltranskey = models.IntegerField(db_column='TillTransKey', blank=True, null=True)  # Field name made lowercase.
    tillsaleamount = models.FloatField(db_column='TillSaleAmount', blank=True, null=True)  # Field name made lowercase.
    tilltransstatus = models.IntegerField(db_column='TillTransStatus', blank=True, null=True)  # Field name made lowercase.
    tillauthcode = models.CharField(db_column='TillAuthCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tillbankname = models.CharField(db_column='TillBankName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bbk_tillmaster'


class BbkTilltransactions(models.Model):
    bbk_transno = models.AutoField(db_column='bbk_TransNo', primary_key=True)  # Field name made lowercase.
    bbk_billno = models.IntegerField(db_column='bbk_BillNo', blank=True, null=True)  # Field name made lowercase.
    bbk_amount = models.FloatField(db_column='bbk_Amount', blank=True, null=True)  # Field name made lowercase.
    bbk_stan = models.CharField(max_length=200, blank=True, null=True)
    bbk_retrefnr = models.CharField(db_column='bbk_retRefNr', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bbk_cardexpiry = models.CharField(db_column='bbk_cardExpiry', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bbk_currency = models.CharField(max_length=200, blank=True, null=True)
    bbk_pan = models.CharField(max_length=200, blank=True, null=True)
    bbk_tid = models.CharField(max_length=200, blank=True, null=True)
    bbk_mid = models.CharField(max_length=200, blank=True, null=True)
    bbk_receiptnr = models.CharField(db_column='bbk_receiptNr', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bbk_scheme = models.CharField(max_length=200, blank=True, null=True)
    bbk_capturetype = models.CharField(db_column='bbk_captureType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bbk_transactiontype = models.CharField(db_column='bbk_transactionType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bbk_signaturerequired = models.CharField(db_column='bbk_signatureRequired', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bbk_pinverified = models.CharField(db_column='bbk_pinVerified', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bbk_authcode = models.CharField(db_column='bbk_authCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bbk_aid = models.CharField(max_length=200, blank=True, null=True)
    bbk_appstartdate = models.CharField(db_column='bbk_appStartDate', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bbk_appexpirydate = models.CharField(db_column='bbk_appExpiryDate', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bbk_apppsn = models.CharField(db_column='bbk_appPSN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bbk_cryptogram = models.CharField(max_length=200, blank=True, null=True)
    bbk_cryptogramtype = models.CharField(db_column='bbk_cryptogramType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bbk_tsi = models.CharField(max_length=200, blank=True, null=True)
    bbk_tvr = models.CharField(max_length=200, blank=True, null=True)
    bbk_cardholdername = models.CharField(db_column='bbk_cardholderName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bbk_tilltransactions'


class Billcleartab(models.Model):
    iblno = models.IntegerField(db_column='IBLno', primary_key=True)  # Field name made lowercase.
    wtnox = models.CharField(db_column='WTnox', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tbno = models.CharField(db_column='TBno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    waiter = models.CharField(db_column='Waiter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibdate = models.DateField(db_column='IBdate', blank=True, null=True)  # Field name made lowercase.
    ibtime = models.CharField(db_column='IBtime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    discpercent = models.FloatField(db_column='DiscPercent', blank=True, null=True)  # Field name made lowercase.
    cash = models.FloatField(db_column='CASH', blank=True, null=True)  # Field name made lowercase.
    clear = models.CharField(db_column='Clear', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pincode = models.CharField(db_column='PinCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paymode = models.CharField(db_column='PayMode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=200, blank=True, null=True)  # Field name made lowercase.
    guestname = models.CharField(db_column='GuestName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    roomnum = models.CharField(db_column='RoomNum', max_length=200, blank=True, null=True)  # Field name made lowercase.
    openbills = models.IntegerField(db_column='OpenBills', blank=True, null=True)  # Field name made lowercase.
    finalbills = models.IntegerField(db_column='FinalBills', blank=True, null=True)  # Field name made lowercase.
    kitords = models.IntegerField(db_column='KitOrds', blank=True, null=True)  # Field name made lowercase.
    nopers = models.IntegerField(db_column='NoPers', blank=True, null=True)  # Field name made lowercase.
    shiftnox = models.CharField(db_column='ShiftNoX', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    ko = models.IntegerField(db_column='KO', blank=True, null=True)  # Field name made lowercase.
    bo = models.IntegerField(db_column='BO', blank=True, null=True)  # Field name made lowercase.
    ob = models.IntegerField(db_column='OB', blank=True, null=True)  # Field name made lowercase.
    fb = models.IntegerField(db_column='FB', blank=True, null=True)  # Field name made lowercase.
    fp = models.IntegerField(db_column='FP', blank=True, null=True)  # Field name made lowercase.
    billtypeid = models.CharField(db_column='BillTypeID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    roomservice = models.CharField(db_column='RoomService', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accperiod = models.IntegerField(db_column='AccPeriod', blank=True, null=True)  # Field name made lowercase.
    cashiername = models.CharField(db_column='CashierName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    barcode = models.FloatField(db_column='BarCode', blank=True, null=True)  # Field name made lowercase.
    orderconcurr = models.CharField(db_column='OrderConcurr', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accno = models.FloatField(db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    g_card = models.CharField(db_column='G_Card', max_length=200, blank=True, null=True)  # Field name made lowercase.
    disccomment = models.CharField(db_column='DiscComment', max_length=200, blank=True, null=True)  # Field name made lowercase.
    discamount = models.FloatField(db_column='DiscAmount', blank=True, null=True)  # Field name made lowercase.
    discounted = models.CharField(db_column='Discounted', max_length=200)  # Field name made lowercase.
    discname = models.CharField(db_column='DiscName', max_length=200)  # Field name made lowercase.
    covers = models.FloatField(db_column='Covers', blank=True, null=True)  # Field name made lowercase.
    serviceperiod = models.CharField(db_column='ServicePeriod', max_length=200, blank=True, null=True)  # Field name made lowercase.
    revcentername = models.CharField(db_column='RevCenterName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cleartime = models.CharField(db_column='ClearTime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    billcreatetime = models.DateTimeField(db_column='BillCreateTime', blank=True, null=True)  # Field name made lowercase.
    print_bill = models.IntegerField(db_column='Print_Bill', blank=True, null=True)  # Field name made lowercase.
    print_order = models.IntegerField(db_column='Print_Order', blank=True, null=True)  # Field name made lowercase.
    salepointname = models.CharField(db_column='SalePointName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bill_orderstatus = models.CharField(db_column='Bill_OrderStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    user_ref = models.FloatField(db_column='user_Ref', blank=True, null=True)  # Field name made lowercase.
    picked = models.IntegerField(db_column='Picked', blank=True, null=True)  # Field name made lowercase.
    batchno = models.IntegerField(db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    entryno = models.IntegerField(db_column='EntryNo', blank=True, null=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    guestaccmap = models.CharField(db_column='GuestAccMap', max_length=200, blank=True, null=True)  # Field name made lowercase.
    billpcname = models.CharField(db_column='BillpcName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    approvedrate = models.CharField(db_column='ApprovedRate', max_length=200, blank=True, null=True)  # Field name made lowercase.
    servedat = models.CharField(db_column='ServedAt', max_length=200, blank=True, null=True)  # Field name made lowercase.
    billcomment = models.CharField(db_column='BillComment', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'billcleartab'


class BillcleartabTemp(models.Model):
    iblno = models.IntegerField(db_column='IBLno', primary_key=True)  # Field name made lowercase.
    wtnox = models.CharField(db_column='WTnox', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tbno = models.CharField(db_column='TBno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    waiter = models.CharField(db_column='Waiter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibdate = models.DateField(db_column='IBdate', blank=True, null=True)  # Field name made lowercase.
    ibtime = models.CharField(db_column='IBtime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    discpercent = models.FloatField(db_column='DiscPercent', blank=True, null=True)  # Field name made lowercase.
    cash = models.FloatField(db_column='CASH', blank=True, null=True)  # Field name made lowercase.
    clear = models.CharField(db_column='Clear', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pincode = models.CharField(db_column='PinCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paymode = models.CharField(db_column='PayMode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=200, blank=True, null=True)  # Field name made lowercase.
    guestname = models.CharField(db_column='GuestName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    roomnum = models.CharField(db_column='RoomNum', max_length=200, blank=True, null=True)  # Field name made lowercase.
    openbills = models.IntegerField(db_column='OpenBills', blank=True, null=True)  # Field name made lowercase.
    finalbills = models.IntegerField(db_column='FinalBills', blank=True, null=True)  # Field name made lowercase.
    kitords = models.IntegerField(db_column='KitOrds', blank=True, null=True)  # Field name made lowercase.
    nopers = models.IntegerField(db_column='NoPers', blank=True, null=True)  # Field name made lowercase.
    shiftnox = models.CharField(db_column='ShiftNoX', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    ko = models.IntegerField(db_column='KO', blank=True, null=True)  # Field name made lowercase.
    bo = models.IntegerField(db_column='BO', blank=True, null=True)  # Field name made lowercase.
    ob = models.IntegerField(db_column='OB', blank=True, null=True)  # Field name made lowercase.
    fb = models.IntegerField(db_column='FB', blank=True, null=True)  # Field name made lowercase.
    fp = models.IntegerField(db_column='FP', blank=True, null=True)  # Field name made lowercase.
    billtypeid = models.CharField(db_column='BillTypeID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    roomservice = models.CharField(db_column='RoomService', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accperiod = models.IntegerField(db_column='AccPeriod', blank=True, null=True)  # Field name made lowercase.
    cashiername = models.CharField(db_column='CashierName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    barcode = models.FloatField(db_column='BarCode', blank=True, null=True)  # Field name made lowercase.
    orderconcurr = models.CharField(db_column='OrderConcurr', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accno = models.FloatField(db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    g_card = models.CharField(db_column='G_Card', max_length=200, blank=True, null=True)  # Field name made lowercase.
    disccomment = models.CharField(db_column='DiscComment', max_length=200, blank=True, null=True)  # Field name made lowercase.
    discamount = models.FloatField(db_column='DiscAmount', blank=True, null=True)  # Field name made lowercase.
    discounted = models.CharField(db_column='Discounted', max_length=200)  # Field name made lowercase.
    discname = models.CharField(db_column='DiscName', max_length=200)  # Field name made lowercase.
    covers = models.FloatField(db_column='Covers', blank=True, null=True)  # Field name made lowercase.
    serviceperiod = models.CharField(db_column='ServicePeriod', max_length=200, blank=True, null=True)  # Field name made lowercase.
    revcentername = models.CharField(db_column='RevCenterName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cleartime = models.CharField(db_column='ClearTime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    billcreatetime = models.DateTimeField(db_column='BillCreateTime', blank=True, null=True)  # Field name made lowercase.
    print_bill = models.IntegerField(db_column='Print_Bill', blank=True, null=True)  # Field name made lowercase.
    print_order = models.IntegerField(db_column='Print_Order', blank=True, null=True)  # Field name made lowercase.
    salepointname = models.CharField(db_column='SalePointName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bill_orderstatus = models.CharField(db_column='Bill_OrderStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    user_ref = models.FloatField(db_column='user_Ref', blank=True, null=True)  # Field name made lowercase.
    pricelist = models.CharField(db_column='PriceList', max_length=200, blank=True, null=True)  # Field name made lowercase.
    guestaccmap = models.CharField(db_column='GuestAccMap', max_length=200, blank=True, null=True)  # Field name made lowercase.
    billpcname = models.CharField(db_column='BillpcName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    servedat = models.CharField(db_column='ServedAt', max_length=200, blank=True, null=True)  # Field name made lowercase.
    billcomment = models.CharField(db_column='BillComment', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'billcleartab_temp'


class Billsettingstbl(models.Model):
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    descrip = models.CharField(db_column='Descrip', max_length=200, blank=True, null=True)  # Field name made lowercase.
    defaultvalue = models.CharField(db_column='DefaultValue', max_length=200, blank=True, null=True)  # Field name made lowercase.
    showonbill = models.CharField(db_column='ShowOnBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    billcaption = models.CharField(db_column='BillCaption', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'billsettingstbl'


class Billvoidheader(models.Model):
    iblno = models.IntegerField(db_column='IBLno', primary_key=True)  # Field name made lowercase.
    wtnox = models.CharField(db_column='WTnox', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tbno = models.CharField(db_column='TBno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    waiter = models.CharField(db_column='Waiter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibdate = models.DateField(db_column='IBdate', blank=True, null=True)  # Field name made lowercase.
    ibtime = models.CharField(db_column='IBtime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    discpercent = models.FloatField(db_column='DiscPercent', blank=True, null=True)  # Field name made lowercase.
    cash = models.FloatField(db_column='CASH', blank=True, null=True)  # Field name made lowercase.
    clear = models.CharField(db_column='Clear', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pincode = models.CharField(db_column='PinCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paymode = models.CharField(db_column='PayMode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=200, blank=True, null=True)  # Field name made lowercase.
    guestname = models.CharField(db_column='GuestName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    roomnum = models.CharField(db_column='RoomNum', max_length=200, blank=True, null=True)  # Field name made lowercase.
    openbills = models.IntegerField(db_column='OpenBills', blank=True, null=True)  # Field name made lowercase.
    finalbills = models.IntegerField(db_column='FinalBills', blank=True, null=True)  # Field name made lowercase.
    kitords = models.IntegerField(db_column='KitOrds', blank=True, null=True)  # Field name made lowercase.
    nopers = models.IntegerField(db_column='NoPers', blank=True, null=True)  # Field name made lowercase.
    shiftnox = models.CharField(db_column='ShiftNoX', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    ko = models.IntegerField(db_column='KO', blank=True, null=True)  # Field name made lowercase.
    bo = models.IntegerField(db_column='BO', blank=True, null=True)  # Field name made lowercase.
    ob = models.IntegerField(db_column='OB', blank=True, null=True)  # Field name made lowercase.
    fb = models.IntegerField(db_column='FB', blank=True, null=True)  # Field name made lowercase.
    fp = models.IntegerField(db_column='FP', blank=True, null=True)  # Field name made lowercase.
    billtypeid = models.CharField(db_column='BillTypeID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    roomservice = models.CharField(db_column='RoomService', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accperiod = models.IntegerField(db_column='AccPeriod', blank=True, null=True)  # Field name made lowercase.
    cashiername = models.CharField(db_column='CashierName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    barcode = models.FloatField(db_column='BarCode', blank=True, null=True)  # Field name made lowercase.
    orderconcurr = models.CharField(db_column='OrderConcurr', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accno = models.FloatField(db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    g_card = models.CharField(db_column='G_Card', max_length=200, blank=True, null=True)  # Field name made lowercase.
    disccomment = models.CharField(db_column='DiscComment', max_length=200, blank=True, null=True)  # Field name made lowercase.
    discamount = models.FloatField(db_column='DiscAmount', blank=True, null=True)  # Field name made lowercase.
    discounted = models.CharField(db_column='Discounted', max_length=200)  # Field name made lowercase.
    discname = models.CharField(db_column='DiscName', max_length=200)  # Field name made lowercase.
    covers = models.FloatField(db_column='Covers', blank=True, null=True)  # Field name made lowercase.
    serviceperiod = models.CharField(db_column='ServicePeriod', max_length=200, blank=True, null=True)  # Field name made lowercase.
    revcentername = models.CharField(db_column='RevCenterName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cleartime = models.CharField(db_column='ClearTime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    billcreatetime = models.DateTimeField(db_column='BillCreateTime', blank=True, null=True)  # Field name made lowercase.
    print_bill = models.IntegerField(db_column='Print_Bill', blank=True, null=True)  # Field name made lowercase.
    print_order = models.IntegerField(db_column='Print_Order', blank=True, null=True)  # Field name made lowercase.
    salepointname = models.CharField(db_column='SalePointName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bill_orderstatus = models.CharField(db_column='Bill_OrderStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    user_ref = models.FloatField(db_column='user_Ref', blank=True, null=True)  # Field name made lowercase.
    picked = models.IntegerField(db_column='Picked', blank=True, null=True)  # Field name made lowercase.
    batchno = models.IntegerField(db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    entryno = models.IntegerField(db_column='EntryNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'billvoidheader'


class Cashierpaymodetots(models.Model):
    totsid = models.AutoField(db_column='TotsID', primary_key=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    paymode = models.CharField(db_column='Paymode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cashierpaymodetots'


class Cattemptab(models.Model):
    inum = models.AutoField(db_column='iNum', primary_key=True)  # Field name made lowercase.
    postto = models.CharField(db_column='PostTo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paymode = models.CharField(db_column='Paymode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    ibdate = models.DateField(db_column='iBdate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cattemptab'


class Comdettab(models.Model):
    xxx = models.CharField(db_column='XXX', primary_key=True, max_length=200)  # Field name made lowercase.
    codenum = models.CharField(db_column='CodeNum', max_length=200)  # Field name made lowercase.
    hotelplusid = models.IntegerField(db_column='HotelPlusID', blank=True, null=True)  # Field name made lowercase.
    biztype = models.CharField(db_column='BizType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=200, blank=True, null=True)  # Field name made lowercase.
    town = models.CharField(db_column='Town', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=200, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pin = models.CharField(db_column='PIN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    vat = models.CharField(db_column='VAT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    trialtimes = models.FloatField(db_column='TrialTimes', blank=True, null=True)  # Field name made lowercase.
    trialmax = models.FloatField(db_column='TrialMax', blank=True, null=True)  # Field name made lowercase.
    fullversion = models.CharField(db_column='FullVersion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    picture1 = models.CharField(db_column='Picture1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    barname = models.CharField(db_column='BarName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dayshifts = models.IntegerField(db_column='DayShifts', blank=True, null=True)  # Field name made lowercase.
    posting = models.CharField(db_column='Posting', max_length=200, blank=True, null=True)  # Field name made lowercase.
    receipttype = models.CharField(db_column='ReceiptType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    recprintdefault = models.CharField(db_column='RecPrintDefault', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fiscalprinterport = models.IntegerField(db_column='FiscalPrinterPort', blank=True, null=True)  # Field name made lowercase.
    poledisplayport = models.IntegerField(db_column='PoleDisplayPort', blank=True, null=True)  # Field name made lowercase.
    showvat = models.CharField(db_column='ShowVat', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cadiffrec = models.CharField(db_column='CadiffRec', max_length=200, blank=True, null=True)  # Field name made lowercase.
    irestlistid = models.CharField(db_column='iRestListID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isourcename = models.CharField(db_column='iSourceName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    allowadjuststock = models.CharField(db_column='AllowAdjustStock', max_length=200, blank=True, null=True)  # Field name made lowercase.
    groupreceiptitems = models.CharField(db_column='GroupReceiptItems', max_length=200, blank=True, null=True)  # Field name made lowercase.
    taxcalcmode = models.CharField(db_column='TaxCalcMode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    multicurr = models.CharField(db_column='MultiCurr', max_length=25, blank=True, null=True)  # Field name made lowercase.
    clientref = models.IntegerField(db_column='ClientRef', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comdettab'
        unique_together = (('xxx', 'codenum'),)


class Commandbuttonstab(models.Model):
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    buttonid = models.CharField(db_column='ButtonID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    buttoncaption = models.CharField(db_column='ButtonCaption', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commandbuttonstab'


class Costingtbl(models.Model):
    costid = models.IntegerField(db_column='CostId', blank=True, null=True)  # Field name made lowercase.
    costname = models.CharField(db_column='CostName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=200, blank=True, null=True)  # Field name made lowercase.
    trackid = models.AutoField(db_column='TrackId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'costingtbl'


class Currenciestbl(models.Model):
    autonum = models.AutoField(db_column='AutoNum', primary_key=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=200, blank=True, null=True)  # Field name made lowercase.
    currrate = models.FloatField(db_column='CurrRate', blank=True, null=True)  # Field name made lowercase.
    basecurr = models.CharField(db_column='BaseCurr', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pricecode = models.FloatField(db_column='PriceCode', blank=True, null=True)  # Field name made lowercase.
    curr_code = models.FloatField(db_column='Curr_Code', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currenciestbl'


class Datedtab(models.Model):
    datecode = models.CharField(db_column='DateCode', primary_key=True, max_length=200)  # Field name made lowercase.
    stadate = models.DateField(db_column='StaDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    lastitemcode = models.CharField(db_column='LastItemCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    setwaiter = models.CharField(db_column='SetWaiter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paymode1 = models.CharField(db_column='PayMode1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftno1 = models.CharField(db_column='ShiftNo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftno1starttime = models.CharField(db_column='ShiftNo1StartTime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    backups = models.CharField(db_column='BackUps', max_length=200, blank=True, null=True)  # Field name made lowercase.
    startibno = models.CharField(db_column='StartIBno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    startibnox = models.CharField(db_column='StartIBnoX', max_length=200, blank=True, null=True)  # Field name made lowercase.
    recptmsg1 = models.CharField(db_column='RecptMsg1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    recptmsg2 = models.CharField(db_column='RecptMsg2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    recptmsg3 = models.CharField(db_column='RecptMsg3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibstart = models.CharField(db_column='IBstart', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftnum = models.CharField(db_column='ShiftNum', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibnotrans = models.CharField(db_column='IBnoTrans', max_length=200, blank=True, null=True)  # Field name made lowercase.
    selbilltime = models.CharField(db_column='SelBillTime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    staffdisc = models.FloatField(db_column='StaffDisc', blank=True, null=True)  # Field name made lowercase.
    guestdisc = models.FloatField(db_column='GuestDisc', blank=True, null=True)  # Field name made lowercase.
    roomservice = models.FloatField(db_column='RoomService', blank=True, null=True)  # Field name made lowercase.
    creditposting = models.CharField(db_column='CreditPosting', max_length=200, blank=True, null=True)  # Field name made lowercase.
    remindpuplicatebill = models.CharField(db_column='RemindPuplicateBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stopaddonceprinted = models.CharField(db_column='StopAddOncePrinted', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mustsendorders = models.CharField(db_column='MustSendOrders', max_length=200, blank=True, null=True)  # Field name made lowercase.
    showpriceonorder = models.CharField(db_column='ShowPriceOnOrder', max_length=200, blank=True, null=True)  # Field name made lowercase.
    roomonbill = models.CharField(db_column='RoomOnBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    signonbill = models.CharField(db_column='SignOnBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    guestonbill = models.CharField(db_column='GuestOnBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    showguestbal = models.CharField(db_column='ShowGuestBal', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ivat = models.FloatField(db_column='iVat', blank=True, null=True)  # Field name made lowercase.
    disctypestaff = models.CharField(db_column='DiscTypeStaff', max_length=200, blank=True, null=True)  # Field name made lowercase.
    clevy = models.FloatField(db_column='CLevy', blank=True, null=True)  # Field name made lowercase.
    scharge = models.FloatField(db_column='SCharge', blank=True, null=True)  # Field name made lowercase.
    disctypeguest = models.CharField(db_column='DiscTypeGuest', max_length=200, blank=True, null=True)  # Field name made lowercase.
    delunsentorders = models.CharField(db_column='DelUnsentOrders', max_length=200, blank=True, null=True)  # Field name made lowercase.
    listwaiters = models.CharField(db_column='ListWaiters', max_length=200, blank=True, null=True)  # Field name made lowercase.
    allowrevert = models.CharField(db_column='AllowRevert', max_length=200, blank=True, null=True)  # Field name made lowercase.
    allowrecswitch = models.CharField(db_column='AllowRecSwitch', max_length=200, blank=True, null=True)  # Field name made lowercase.
    appendsourceid = models.CharField(db_column='AppendSourceId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    postsingleitems = models.CharField(db_column='PostSingleItems', max_length=200, blank=True, null=True)  # Field name made lowercase.
    showdescriptiononbill = models.CharField(db_column='ShowDescriptionOnBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mcintergration = models.CharField(db_column='MCintergration', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sourceordersets = models.CharField(db_column='SourceOrderSets', max_length=200, blank=True, null=True)  # Field name made lowercase.
    enablemultipaymode = models.CharField(db_column='EnableMultiPaymode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pickcurrprice = models.CharField(db_column='PickCurrPrice', max_length=200, blank=True, null=True)  # Field name made lowercase.
    statementbillitems = models.CharField(db_column='StatementBillItems', max_length=200, blank=True, null=True)  # Field name made lowercase.
    potraitrpt = models.CharField(db_column='PotraitRpt', max_length=200, blank=True, null=True)  # Field name made lowercase.
    header = models.CharField(db_column='Header', max_length=200, blank=True, null=True)  # Field name made lowercase.
    activatepos = models.CharField(db_column='ActivatePOS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    posdefaultsource = models.CharField(db_column='POSDefaultSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    userapidesd = models.CharField(db_column='UseRapidESD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    checkwbfirst = models.CharField(db_column='CheckWBFirst', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rapidsignreport = models.CharField(db_column='RapidSignReport', max_length=200, blank=True, null=True)  # Field name made lowercase.
    showdupcaption = models.CharField(db_column='ShowDupCaption', max_length=200, blank=True, null=True)  # Field name made lowercase.
    blocktableinuse = models.CharField(db_column='BlockTableInUse', max_length=200, blank=True, null=True)  # Field name made lowercase.
    batchorder = models.CharField(db_column='BatchOrder', max_length=200, blank=True, null=True)  # Field name made lowercase.
    batchbill = models.CharField(db_column='BatchBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    showlogo = models.CharField(db_column='ShowLogo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    batchbilloption = models.IntegerField(db_column='BatchBillOption', blank=True, null=True)  # Field name made lowercase.
    showguestroom = models.CharField(db_column='ShowGuestRoom', max_length=200, blank=True, null=True)  # Field name made lowercase.
    showwaitertable = models.CharField(db_column='ShowWaiterTable', max_length=200, blank=True, null=True)  # Field name made lowercase.
    allowtypingtablno = models.CharField(db_column='AllowTypingTablNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kitchendisplaycomp = models.CharField(db_column='KitchenDisplayComp', max_length=200, blank=True, null=True)  # Field name made lowercase.
    customerdisplaycomp = models.CharField(db_column='CustomerDisplayComp', max_length=200, blank=True, null=True)  # Field name made lowercase.
    showordernumonbill = models.CharField(db_column='ShowOrderNumOnBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    generateordernum = models.CharField(db_column='GenerateOrderNum', max_length=200, blank=True, null=True)  # Field name made lowercase.
    waitersordercopy = models.CharField(db_column='WaitersOrderCopy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    usememberpricelist = models.CharField(db_column='UseMemberPriceList', max_length=200, blank=True, null=True)  # Field name made lowercase.
    voidclearedonly = models.CharField(db_column='VoidClearedOnly', max_length=200, blank=True, null=True)  # Field name made lowercase.
    useticketingprinter = models.CharField(db_column='UseTicketingPrinter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    socketport = models.IntegerField(db_column='SocketPort', blank=True, null=True)  # Field name made lowercase.
    closefrontinv = models.CharField(db_column='CloseFrontInv', max_length=200, blank=True, null=True)  # Field name made lowercase.
    compapproval = models.CharField(db_column='CompApproval', max_length=20, blank=True, null=True)  # Field name made lowercase.
    showbasecurrtotal = models.CharField(db_column='ShowBaseCurrTotal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stopenddayunposted = models.CharField(db_column='StopEndDayUnposted', max_length=200, blank=True, null=True)  # Field name made lowercase.
    showbasecurrtotbill = models.CharField(db_column='ShowBaseCurrTotBill', max_length=20, blank=True, null=True)  # Field name made lowercase.
    showdecimal = models.CharField(db_column='ShowDecimal', max_length=200, blank=True, null=True)  # Field name made lowercase.
    eatincaption = models.CharField(db_column='EatInCaption', max_length=200, blank=True, null=True)  # Field name made lowercase.
    newbillcaption = models.CharField(db_column='NewBillCaption', max_length=200, blank=True, null=True)  # Field name made lowercase.
    printbillcaption = models.CharField(db_column='PrintBillCaption', max_length=200, blank=True, null=True)  # Field name made lowercase.
    selectbillcaption = models.CharField(db_column='SelectBillCaption', max_length=200, blank=True, null=True)  # Field name made lowercase.
    billnocaption = models.CharField(db_column='BillNOCaption', max_length=200, blank=True, null=True)  # Field name made lowercase.
    recipecaption = models.CharField(db_column='RecipeCaption', max_length=200, blank=True, null=True)  # Field name made lowercase.
    showqronbill = models.CharField(db_column='ShowQROnBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dontsellzerorecipes = models.CharField(db_column='DontSellZeroRecipes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qrurl = models.CharField(db_column='QRurl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    revertonpos = models.CharField(db_column='RevertOnPOS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    clearcaption = models.CharField(db_column='ClearCaption', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tacaption = models.CharField(db_column='TACaption', max_length=200, blank=True, null=True)  # Field name made lowercase.
    billcaption = models.CharField(db_column='BillCaption', max_length=200, blank=True, null=True)  # Field name made lowercase.
    receiptcaption = models.CharField(db_column='ReceiptCaption', max_length=200, blank=True, null=True)  # Field name made lowercase.
    billtaxcaption = models.CharField(db_column='BillTaxCaption', max_length=200, blank=True, null=True)  # Field name made lowercase.
    showtaxonbill = models.CharField(db_column='ShowTaxOnBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    showtaxonreceipt = models.CharField(db_column='ShowTaxOnReceipt', max_length=200, blank=True, null=True)  # Field name made lowercase.
    showtaxbonbill = models.CharField(db_column='ShowTaxBOnBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    autostartfloat = models.CharField(db_column='AutoStartFloat', max_length=200, blank=True, null=True)  # Field name made lowercase.
    hidebuttonsonpos = models.CharField(db_column='HideButtonsonPOS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    batchreceipt = models.CharField(db_column='BatchReceipt', max_length=200, blank=True, null=True)  # Field name made lowercase.
    openregister = models.CharField(db_column='OpenRegister', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stopcheckstockbal = models.CharField(db_column='StopCheckStockBal', max_length=200, blank=True, null=True)  # Field name made lowercase.
    miscellenousdisplaycomp = models.CharField(db_column='MiscellenousDisplayComp', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kitsource = models.CharField(db_column='kitSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    miscsource = models.CharField(db_column='MiscSource', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datedtab'


class Deletedtab(models.Model):
    iblno = models.CharField(db_column='IBLno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tbno = models.CharField(db_column='TBno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wtname = models.CharField(db_column='WTname', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibtime = models.CharField(db_column='IBtime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qnty = models.IntegerField(db_column='Qnty', blank=True, null=True)  # Field name made lowercase.
    ppu = models.FloatField(db_column='PPU', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibdate = models.DateField(db_column='IBdate', blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    postedby = models.CharField(db_column='PostedBy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    guestname = models.CharField(db_column='GuestName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    workstationname = models.CharField(db_column='WorkstationName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    refsauto = models.IntegerField(db_column='RefSAuto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deletedtab'


class Denominationstbl(models.Model):
    transid = models.AutoField(db_column='Transid', primary_key=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    displaytext = models.CharField(db_column='DisplayText', max_length=200, blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'denominationstbl'


class Depttbl(models.Model):
    transid = models.AutoField(db_column='TransId', primary_key=True)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isdel = models.CharField(db_column='isDel', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'depttbl'


class Discountstable(models.Model):
    billno = models.CharField(db_column='BillNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    waiter = models.CharField(db_column='Waiter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    time1 = models.CharField(db_column='Time1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    date1 = models.CharField(db_column='Date1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    discperc = models.FloatField(db_column='DiscPerc', blank=True, null=True)  # Field name made lowercase.
    discamount = models.FloatField(db_column='DiscAmount', blank=True, null=True)  # Field name made lowercase.
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    billamount = models.FloatField(db_column='BillAmount', blank=True, null=True)  # Field name made lowercase.
    discdesc = models.CharField(db_column='DiscDesc', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'discountstable'


class Extravaganza(models.Model):
    transid = models.AutoField(db_column='TransID', primary_key=True)  # Field name made lowercase.
    storecode = models.IntegerField(db_column='StoreCode', blank=True, null=True)  # Field name made lowercase.
    storename = models.CharField(db_column='StoreName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=200, blank=True, null=True)  # Field name made lowercase.
    poscode = models.IntegerField(db_column='PosCode', blank=True, null=True)  # Field name made lowercase.
    posname = models.CharField(db_column='PosName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    posunits = models.CharField(db_column='PosUnits', max_length=200, blank=True, null=True)  # Field name made lowercase.
    convertqty = models.FloatField(db_column='ConvertQty', blank=True, null=True)  # Field name made lowercase.
    reorderqty = models.FloatField(db_column='ReorderQty', blank=True, null=True)  # Field name made lowercase.
    available = models.FloatField(db_column='Available', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'extravaganza'


class Foodcosttbl(models.Model):
    icosttransid = models.AutoField(db_column='iCostTransID', primary_key=True)  # Field name made lowercase.
    icost_shiftno = models.IntegerField(db_column='iCost_ShiftNo', blank=True, null=True)  # Field name made lowercase.
    icost_itemsource = models.CharField(db_column='iCost_ItemSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    icost_totalsales = models.FloatField(db_column='iCost_TotalSales', blank=True, null=True)  # Field name made lowercase.
    icost_totalcost = models.FloatField(db_column='iCost_TotalCost', blank=True, null=True)  # Field name made lowercase.
    icost_fcost = models.FloatField(db_column='iCost_FCost', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'foodcosttbl'


class Gueststab(models.Model):
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    guestname = models.CharField(db_column='GuestName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gueststab'


class Happyhourtbl(models.Model):
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    dayofwk = models.CharField(db_column='DayofWk', max_length=200, blank=True, null=True)  # Field name made lowercase.
    happyfrom = models.IntegerField(db_column='HappyFrom', blank=True, null=True)  # Field name made lowercase.
    happyto = models.IntegerField(db_column='HappyTo', blank=True, null=True)  # Field name made lowercase.
    itemgroup = models.CharField(db_column='ItemGroup', max_length=200, blank=True, null=True)  # Field name made lowercase.
    disc = models.FloatField(db_column='Disc', blank=True, null=True)  # Field name made lowercase.
    discstatus = models.CharField(db_column='DiscStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    disctype = models.CharField(db_column='DiscType', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'happyhourtbl'


class Ibcurrenttab(models.Model):
    autonox = models.CharField(db_column='AutoNoX', primary_key=True, max_length=200)  # Field name made lowercase.
    ibno = models.CharField(db_column='IBno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tbno = models.CharField(db_column='TBno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wtno = models.CharField(db_column='WTno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibtime = models.CharField(db_column='IBtime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibdate = models.CharField(db_column='IBdate', max_length=200, blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    discpercent = models.FloatField(db_column='DiscPercent', blank=True, null=True)  # Field name made lowercase.
    discamount = models.FloatField(db_column='DiscAmount', blank=True, null=True)  # Field name made lowercase.
    finamount = models.FloatField(db_column='FinAmount', blank=True, null=True)  # Field name made lowercase.
    cash = models.FloatField(db_column='CASH', blank=True, null=True)  # Field name made lowercase.
    change = models.FloatField(db_column='CHANGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ibcurrenttab'


class Ibsalestab(models.Model):
    sautonum = models.AutoField(db_column='SautoNum', primary_key=True)  # Field name made lowercase.
    iblno = models.IntegerField(db_column='IBLno', blank=True, null=True)  # Field name made lowercase.
    tbno = models.CharField(db_column='TBno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    waiter = models.CharField(db_column='Waiter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibtime = models.CharField(db_column='IBtime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibdate = models.DateField(db_column='IBdate', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemstab', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ittime = models.CharField(db_column='ITtime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qnty = models.IntegerField(db_column='Qnty', blank=True, null=True)  # Field name made lowercase.
    ppu = models.FloatField(db_column='PPU', blank=True, null=True)  # Field name made lowercase.
    prodgrp = models.CharField(db_column='ProdGrp', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wrent = models.CharField(db_column='WrEnt', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sourcecat = models.CharField(db_column='SourceCat', max_length=200, blank=True, null=True)  # Field name made lowercase.
    postto = models.CharField(db_column='PostTo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    guestname = models.CharField(db_column='GuestName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    roomnum = models.CharField(db_column='RoomNum', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paymode = models.CharField(db_column='Paymode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemsource = models.CharField(db_column='ItemSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    storecode = models.CharField(db_column='StoreCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    costcode = models.CharField(db_column='CostCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    unitcost = models.FloatField(db_column='UnitCost', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=200, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.IntegerField(db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    disctype = models.IntegerField(db_column='DiscType', blank=True, null=True)  # Field name made lowercase.
    discperc = models.FloatField(db_column='DiscPerc', blank=True, null=True)  # Field name made lowercase.
    storetype = models.CharField(db_column='StoreType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accperiod = models.IntegerField(db_column='AccPeriod', blank=True, null=True)  # Field name made lowercase.
    iresttxnid = models.CharField(db_column='iRestTxnID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ipaytxnid = models.CharField(db_column='iPayTxnID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    barcode = models.FloatField(db_column='BarCode', blank=True, null=True)  # Field name made lowercase.
    exactqty = models.FloatField(db_column='ExactQty', blank=True, null=True)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idisctype = models.CharField(db_column='iDiscType', max_length=200)  # Field name made lowercase.
    discamt = models.FloatField(db_column='DiscAmt', blank=True, null=True)  # Field name made lowercase.
    aliasname = models.CharField(db_column='AliasName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ishappyhour = models.CharField(db_column='isHappyHour', max_length=200, blank=True, null=True)  # Field name made lowercase.
    serviceperiod = models.CharField(db_column='ServicePeriod', max_length=200, blank=True, null=True)  # Field name made lowercase.
    servicetime = models.DateTimeField(db_column='ServiceTime', blank=True, null=True)  # Field name made lowercase.
    taxa = models.FloatField(db_column='TaxA', blank=True, null=True)  # Field name made lowercase.
    taxb = models.FloatField(db_column='TaxB', blank=True, null=True)  # Field name made lowercase.
    taxc = models.FloatField(db_column='TaxC', blank=True, null=True)  # Field name made lowercase.
    taxamount = models.FloatField(db_column='TaxAmount', blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ordernum = models.FloatField(db_column='OrderNum', blank=True, null=True)  # Field name made lowercase.
    tempppu = models.FloatField(db_column='TempPPU', blank=True, null=True)  # Field name made lowercase.
    posttoaccmap = models.CharField(db_column='PosttoAccMap', max_length=200, blank=True, null=True)  # Field name made lowercase.
    irefnumid = models.CharField(db_column='iRefNumID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    postpcname = models.CharField(db_column='PostPcName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    countqty = models.IntegerField(db_column='CountQty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ibsalestab'


class IbsalestabTemp(models.Model):
    sautonum = models.AutoField(db_column='SautoNum', primary_key=True)  # Field name made lowercase.
    iblno = models.IntegerField(db_column='IBLno', blank=True, null=True)  # Field name made lowercase.
    tbno = models.CharField(db_column='TBno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    waiter = models.CharField(db_column='Waiter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibtime = models.CharField(db_column='IBtime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibdate = models.DateField(db_column='IBdate', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ittime = models.CharField(db_column='ITtime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qnty = models.IntegerField(db_column='Qnty', blank=True, null=True)  # Field name made lowercase.
    ppu = models.FloatField(db_column='PPU', blank=True, null=True)  # Field name made lowercase.
    prodgrp = models.CharField(db_column='ProdGrp', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wrent = models.CharField(db_column='WrEnt', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sourcecat = models.CharField(db_column='SourceCat', max_length=200, blank=True, null=True)  # Field name made lowercase.
    postto = models.CharField(db_column='PostTo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    guestname = models.CharField(db_column='GuestName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    roomnum = models.CharField(db_column='RoomNum', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paymode = models.CharField(db_column='Paymode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemsource = models.CharField(db_column='ItemSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    storecode = models.CharField(db_column='StoreCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    costcode = models.CharField(db_column='CostCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    unitcost = models.FloatField(db_column='UnitCost', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=200, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.IntegerField(db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    disctype = models.IntegerField(db_column='DiscType', blank=True, null=True)  # Field name made lowercase.
    discperc = models.FloatField(db_column='DiscPerc', blank=True, null=True)  # Field name made lowercase.
    storetype = models.CharField(db_column='StoreType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accperiod = models.IntegerField(db_column='AccPeriod', blank=True, null=True)  # Field name made lowercase.
    iresttxnid = models.CharField(db_column='iRestTxnID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ipaytxnid = models.CharField(db_column='iPayTxnID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    barcode = models.FloatField(db_column='BarCode', blank=True, null=True)  # Field name made lowercase.
    exactqty = models.FloatField(db_column='ExactQty', blank=True, null=True)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idisctype = models.CharField(db_column='iDiscType', max_length=200)  # Field name made lowercase.
    discamt = models.FloatField(db_column='DiscAmt', blank=True, null=True)  # Field name made lowercase.
    aliasname = models.CharField(db_column='AliasName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ishappyhour = models.CharField(db_column='isHappyHour', max_length=200, blank=True, null=True)  # Field name made lowercase.
    serviceperiod = models.CharField(db_column='ServicePeriod', max_length=200, blank=True, null=True)  # Field name made lowercase.
    servicetime = models.DateTimeField(db_column='ServiceTime', blank=True, null=True)  # Field name made lowercase.
    taxa = models.FloatField(db_column='TaxA', blank=True, null=True)  # Field name made lowercase.
    taxb = models.FloatField(db_column='TaxB', blank=True, null=True)  # Field name made lowercase.
    taxc = models.FloatField(db_column='TaxC', blank=True, null=True)  # Field name made lowercase.
    taxamount = models.FloatField(db_column='TaxAmount', blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ordernum = models.FloatField(db_column='OrderNum', blank=True, null=True)  # Field name made lowercase.
    printed = models.FloatField(db_column='Printed', blank=True, null=True)  # Field name made lowercase.
    tempppu = models.FloatField(db_column='TempPPU', blank=True, null=True)  # Field name made lowercase.
    posttoaccmap = models.CharField(db_column='PosttoAccMap', max_length=200, blank=True, null=True)  # Field name made lowercase.
    irefnumid = models.CharField(db_column='iRefNumID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ilocalstatus = models.IntegerField(db_column='iLocalStatus', blank=True, null=True)  # Field name made lowercase.
    postpcname = models.CharField(db_column='PostPcName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    countqty = models.IntegerField(db_column='CountQty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ibsalestab_temp'


class Imaterialstab(models.Model):
    sautonum = models.AutoField(db_column='SautoNum', primary_key=True)  # Field name made lowercase.
    iblno = models.IntegerField(db_column='IBLno', blank=True, null=True)  # Field name made lowercase.
    ibtime = models.CharField(db_column='IBtime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibdate = models.DateField(db_column='IBdate', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qnty = models.FloatField(db_column='Qnty', blank=True, null=True)  # Field name made lowercase.
    ppu = models.FloatField(db_column='PPU', blank=True, null=True)  # Field name made lowercase.
    prodgrp = models.CharField(db_column='ProdGrp', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sourcecat = models.CharField(db_column='SourceCat', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemsource = models.CharField(db_column='ItemSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=200, blank=True, null=True)  # Field name made lowercase.
    iparentcode = models.IntegerField(db_column='iParentCode', blank=True, null=True)  # Field name made lowercase.
    iparentname = models.CharField(db_column='iParentName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    exactqty = models.FloatField(db_column='ExactQty', blank=True, null=True)  # Field name made lowercase.
    stockbal = models.IntegerField(db_column='StockBal', blank=True, null=True)  # Field name made lowercase.
    posttime = models.DateTimeField(db_column='PostTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'imaterialstab'


class ImaterialstabTemp(models.Model):
    sautonum = models.AutoField(db_column='SautoNum', primary_key=True)  # Field name made lowercase.
    iblno = models.IntegerField(db_column='IBLno', blank=True, null=True)  # Field name made lowercase.
    ibtime = models.CharField(db_column='IBtime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibdate = models.DateField(db_column='IBdate', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qnty = models.FloatField(db_column='Qnty', blank=True, null=True)  # Field name made lowercase.
    ppu = models.FloatField(db_column='PPU', blank=True, null=True)  # Field name made lowercase.
    prodgrp = models.CharField(db_column='ProdGrp', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sourcecat = models.CharField(db_column='SourceCat', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemsource = models.CharField(db_column='ItemSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=200, blank=True, null=True)  # Field name made lowercase.
    iparentcode = models.IntegerField(db_column='iParentCode', blank=True, null=True)  # Field name made lowercase.
    iparentname = models.CharField(db_column='iParentName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    exactqty = models.FloatField(db_column='ExactQty', blank=True, null=True)  # Field name made lowercase.
    stockbal = models.IntegerField(db_column='StockBal', blank=True, null=True)  # Field name made lowercase.
    posttime = models.DateTimeField(db_column='PostTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'imaterialstab_temp'


class Issuessummary(models.Model):
    transno = models.AutoField(db_column='TransNo', primary_key=True)  # Field name made lowercase.
    reqno = models.IntegerField(db_column='ReqNo', blank=True, null=True)  # Field name made lowercase.
    dept = models.CharField(db_column='Dept', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reqdate = models.DateField(db_column='ReqDate', blank=True, null=True)  # Field name made lowercase.
    items = models.FloatField(db_column='Items', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    issueby = models.CharField(db_column='IssueBy', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'issuessummary'


class Issuesview(models.Model):
    issueid = models.AutoField(db_column='IssueID', primary_key=True)  # Field name made lowercase.
    dept = models.CharField(db_column='Dept', max_length=200, blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'issuesview'


class Istocksadded(models.Model):
    itemcode = models.CharField(db_column='ItemCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ucost = models.FloatField(db_column='Ucost', blank=True, null=True)  # Field name made lowercase.
    qstart = models.FloatField(db_column='Qstart', blank=True, null=True)  # Field name made lowercase.
    qadded = models.FloatField(db_column='Qadded', blank=True, null=True)  # Field name made lowercase.
    totalin = models.FloatField(db_column='TotalIn', blank=True, null=True)  # Field name made lowercase.
    qused = models.FloatField(db_column='Qused', blank=True, null=True)  # Field name made lowercase.
    qusedm = models.FloatField(db_column='QusedM', blank=True, null=True)  # Field name made lowercase.
    spoilages = models.FloatField(db_column='Spoilages', blank=True, null=True)  # Field name made lowercase.
    totalout = models.FloatField(db_column='TotalOut', blank=True, null=True)  # Field name made lowercase.
    sysbal = models.FloatField(db_column='SysBal', blank=True, null=True)  # Field name made lowercase.
    phybal = models.FloatField(db_column='PhyBal', blank=True, null=True)  # Field name made lowercase.
    variance = models.FloatField(db_column='Variance', blank=True, null=True)  # Field name made lowercase.
    totalcost = models.FloatField(db_column='TotalCost', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'istocksadded'


class Itemcategories(models.Model):
    code1 = models.AutoField(db_column='Code1', primary_key=True)  # Field name made lowercase.
    itemcategory = models.CharField(db_column='ItemCategory', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemgroup = models.CharField(db_column='ItemGroup', max_length=200, blank=True, null=True)  # Field name made lowercase.
    postto = models.CharField(db_column='PostTo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    buttoncode = models.IntegerField(db_column='ButtonCode', blank=True, null=True)  # Field name made lowercase.
    itemsource = models.CharField(db_column='ItemSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=200, blank=True, null=True)  # Field name made lowercase.
    orderprintstation = models.CharField(db_column='OrderPrintStation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    orderprintername = models.CharField(db_column='OrderPrinterName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    papersize = models.CharField(db_column='PaperSize', max_length=200, blank=True, null=True)  # Field name made lowercase.
    printpreview = models.CharField(db_column='PrintPreview', max_length=200, blank=True, null=True)  # Field name made lowercase.
    copies = models.IntegerField(db_column='Copies', blank=True, null=True)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    happyhourstatus = models.CharField(db_column='HappyHourStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    disctype = models.CharField(db_column='DiscType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    disc = models.FloatField(db_column='Disc', blank=True, null=True)  # Field name made lowercase.
    number_1from = models.IntegerField(db_column='1From', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1to = models.IntegerField(db_column='1To', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2from = models.IntegerField(db_column='2From', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2to = models.IntegerField(db_column='2To', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3from = models.IntegerField(db_column='3From', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3to = models.IntegerField(db_column='3To', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4from = models.IntegerField(db_column='4From', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4to = models.IntegerField(db_column='4To', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5from = models.IntegerField(db_column='5From', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5to = models.IntegerField(db_column='5To', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_6from = models.IntegerField(db_column='6From', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_6to = models.IntegerField(db_column='6To', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_7from = models.IntegerField(db_column='7From', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_7to = models.IntegerField(db_column='7To', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    voidstatus = models.CharField(db_column='VoidStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemlinkable = models.CharField(db_column='ItemLinkable', max_length=200, blank=True, null=True)  # Field name made lowercase.
    commperc = models.FloatField(db_column='CommPerc', blank=True, null=True)  # Field name made lowercase.
    commamt = models.FloatField(db_column='CommAmt', blank=True, null=True)  # Field name made lowercase.
    periodcount = models.FloatField(db_column='PeriodCount', blank=True, null=True)  # Field name made lowercase.
    periodsales = models.FloatField(db_column='PeriodSales', blank=True, null=True)  # Field name made lowercase.
    monthlycount = models.FloatField(db_column='MonthlyCount', blank=True, null=True)  # Field name made lowercase.
    monthlysales = models.FloatField(db_column='MonthlySales', blank=True, null=True)  # Field name made lowercase.
    yearlycount = models.FloatField(db_column='YearlyCount', blank=True, null=True)  # Field name made lowercase.
    yearlysales = models.FloatField(db_column='YearlySales', blank=True, null=True)  # Field name made lowercase.
    periodperc = models.FloatField(db_column='PeriodPerc', blank=True, null=True)  # Field name made lowercase.
    monthlyperc = models.FloatField(db_column='MonthlyPerc', blank=True, null=True)  # Field name made lowercase.
    yearlyperc = models.FloatField(db_column='YearlyPerc', blank=True, null=True)  # Field name made lowercase.
    istaxgroup = models.CharField(db_column='isTaxGroup', max_length=200, blank=True, null=True)  # Field name made lowercase.
    costsalescode = models.CharField(max_length=200, blank=True, null=True)
    isstockable = models.CharField(db_column='isStockable', max_length=20, blank=True, null=True)  # Field name made lowercase.
    marginrangefrom = models.FloatField(db_column='MarginRangeFrom', blank=True, null=True)  # Field name made lowercase.
    marginrangeto = models.FloatField(db_column='MarginRangeTo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itemcategories'


class Itempcomm(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    roomno = models.CharField(db_column='RoomNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    guestname = models.CharField(db_column='GuestName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accname = models.CharField(db_column='AccName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    checkin = models.DateField(db_column='Checkin', blank=True, null=True)  # Field name made lowercase.
    checkout = models.DateField(db_column='CheckOut', blank=True, null=True)  # Field name made lowercase.
    pax = models.FloatField(db_column='Pax', blank=True, null=True)  # Field name made lowercase.
    boardtype = models.CharField(db_column='BoardType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    days = models.IntegerField(db_column='Days', blank=True, null=True)  # Field name made lowercase.
    rate = models.CharField(db_column='Rate', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ratetotal = models.FloatField(db_column='RateTotal', blank=True, null=True)  # Field name made lowercase.
    agent = models.CharField(db_column='Agent', max_length=200, blank=True, null=True)  # Field name made lowercase.
    comm = models.FloatField(db_column='Comm', blank=True, null=True)  # Field name made lowercase.
    roomstatus = models.CharField(db_column='RoomStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=200, blank=True, null=True)  # Field name made lowercase.
    personal = models.CharField(db_column='Personal', max_length=200, blank=True, null=True)  # Field name made lowercase.
    children = models.FloatField(db_column='Children', blank=True, null=True)  # Field name made lowercase.
    accfood = models.FloatField(db_column='AccFood', blank=True, null=True)  # Field name made lowercase.
    accbar = models.FloatField(db_column='AccBar', blank=True, null=True)  # Field name made lowercase.
    guestmisc = models.FloatField(db_column='GuestMisc', blank=True, null=True)  # Field name made lowercase.
    billtotal = models.FloatField(db_column='BillTotal', blank=True, null=True)  # Field name made lowercase.
    net = models.FloatField(db_column='Net', blank=True, null=True)  # Field name made lowercase.
    pricevariance = models.FloatField(db_column='Pricevariance', blank=True, null=True)  # Field name made lowercase.
    costvariance = models.FloatField(db_column='Costvariance', blank=True, null=True)  # Field name made lowercase.
    qtyvariance = models.FloatField(db_column='Qtyvariance', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itempcomm'


class Itempcomm3(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    roomno = models.CharField(db_column='RoomNo', max_length=600, blank=True, null=True)  # Field name made lowercase.
    guestname = models.CharField(db_column='GuestName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accname = models.CharField(db_column='AccName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    checkin = models.DateField(db_column='Checkin', blank=True, null=True)  # Field name made lowercase.
    checkout = models.DateField(db_column='CheckOut', blank=True, null=True)  # Field name made lowercase.
    pax = models.FloatField(db_column='Pax', blank=True, null=True)  # Field name made lowercase.
    boardtype = models.CharField(db_column='BoardType', max_length=600, blank=True, null=True)  # Field name made lowercase.
    days = models.IntegerField(db_column='Days', blank=True, null=True)  # Field name made lowercase.
    rate = models.CharField(db_column='Rate', max_length=600, blank=True, null=True)  # Field name made lowercase.
    ratetotal = models.FloatField(db_column='RateTotal', blank=True, null=True)  # Field name made lowercase.
    agent = models.CharField(db_column='Agent', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comm = models.FloatField(db_column='Comm', blank=True, null=True)  # Field name made lowercase.
    roomstatus = models.CharField(db_column='RoomStatus', max_length=600, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=600, blank=True, null=True)  # Field name made lowercase.
    personal = models.CharField(db_column='Personal', max_length=600, blank=True, null=True)  # Field name made lowercase.
    children = models.FloatField(db_column='Children', blank=True, null=True)  # Field name made lowercase.
    accfood = models.FloatField(db_column='AccFood', blank=True, null=True)  # Field name made lowercase.
    accbar = models.FloatField(db_column='AccBar', blank=True, null=True)  # Field name made lowercase.
    guestmisc = models.FloatField(db_column='GuestMisc', blank=True, null=True)  # Field name made lowercase.
    billtotal = models.FloatField(db_column='BillTotal', blank=True, null=True)  # Field name made lowercase.
    field1 = models.CharField(max_length=600, blank=True, null=True)
    sysbal = models.FloatField(db_column='SysBal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itempcomm3'


class Itemportionstab(models.Model):
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    itemcoderest = models.ForeignKey('Itemstab', models.DO_NOTHING, db_column='ItemCodeRest', blank=True, null=True)  # Field name made lowercase.
    itemnamerest = models.CharField(db_column='ItemNameRest', max_length=200, blank=True, null=True)  # Field name made lowercase.
    unitsrest = models.CharField(db_column='UnitsRest', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ppurest = models.FloatField(db_column='PPUrest', blank=True, null=True)  # Field name made lowercase.
    itemsource = models.CharField(db_column='ItemSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    ucost = models.FloatField(db_column='Ucost', blank=True, null=True)  # Field name made lowercase.
    qrestsoldb4 = models.FloatField(db_column='QrestSoldB4', blank=True, null=True)  # Field name made lowercase.
    qrestsold = models.FloatField(db_column='QrestSold', blank=True, null=True)  # Field name made lowercase.
    qstoreaddedb4 = models.FloatField(db_column='QstoreAddedB4', blank=True, null=True)  # Field name made lowercase.
    qstoreadded = models.FloatField(db_column='QstoreAdded', blank=True, null=True)  # Field name made lowercase.
    recipe_comment = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemportionstab'


class ItemportionstabCopy(models.Model):
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    itemcoderest = models.IntegerField(db_column='ItemCodeRest', blank=True, null=True)  # Field name made lowercase.
    itemnamerest = models.CharField(db_column='ItemNameRest', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemcodestore = models.IntegerField(db_column='ItemCodeStore', blank=True, null=True)  # Field name made lowercase.
    itemnamestore = models.CharField(db_column='ItemNameStore', max_length=300, blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    ucost = models.FloatField(db_column='Ucost', blank=True, null=True)  # Field name made lowercase.
    qrestsoldb4 = models.FloatField(db_column='QrestSoldB4', blank=True, null=True)  # Field name made lowercase.
    qrestsold = models.FloatField(db_column='QrestSold', blank=True, null=True)  # Field name made lowercase.
    qstoreaddedb4 = models.FloatField(db_column='QstoreAddedB4', blank=True, null=True)  # Field name made lowercase.
    qstoreadded = models.FloatField(db_column='QstoreAdded', blank=True, null=True)  # Field name made lowercase.
    storecategory = models.CharField(db_column='StoreCategory', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itemportionstab_copy'


class ItemportionstabCopyx(models.Model):
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    itemcoderest = models.IntegerField(db_column='ItemCodeRest', blank=True, null=True)  # Field name made lowercase.
    itemnamerest = models.CharField(db_column='ItemNameRest', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemsource = models.CharField(db_column='ItemSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    ucost = models.FloatField(db_column='Ucost', blank=True, null=True)  # Field name made lowercase.
    qrestsoldb4 = models.FloatField(db_column='QrestSoldB4', blank=True, null=True)  # Field name made lowercase.
    qrestsold = models.FloatField(db_column='QrestSold', blank=True, null=True)  # Field name made lowercase.
    qstoreaddedb4 = models.FloatField(db_column='QstoreAddedB4', blank=True, null=True)  # Field name made lowercase.
    qstoreadded = models.FloatField(db_column='QstoreAdded', blank=True, null=True)  # Field name made lowercase.
    storecategoryx = models.CharField(db_column='StoreCategoryX', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itemportionstab_copyx'


class Itemsdesctab(models.Model):
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    descrip = models.CharField(db_column='Descrip', max_length=200, blank=True, null=True)  # Field name made lowercase.
    descstep = models.IntegerField(db_column='DescStep', blank=True, null=True)  # Field name made lowercase.
    desccode = models.IntegerField(db_column='DescCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itemsdesctab'


class Itemspricelist(models.Model):
    transno = models.AutoField(db_column='TransNo', primary_key=True)  # Field name made lowercase.
    price_itemcode = models.IntegerField(db_column='Price_itemCode', blank=True, null=True)  # Field name made lowercase.
    price_itemname = models.CharField(db_column='Price_ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    price_pricegroupname = models.CharField(db_column='Price_PriceGroupName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    price_priceamount = models.FloatField(db_column='Price_PriceAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itemspricelist'


class Itemstab(models.Model):
    itemcode = models.AutoField(db_column='ItemCode', primary_key=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    prodgr = models.CharField(db_column='ProdGr', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sourcecat = models.CharField(db_column='SourceCat', max_length=200, blank=True, null=True)  # Field name made lowercase.
    postto = models.CharField(db_column='PostTo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qnty = models.IntegerField(db_column='Qnty', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ucost = models.FloatField(db_column='Ucost', blank=True, null=True)  # Field name made lowercase.
    qpurch = models.FloatField(db_column='QPurch', blank=True, null=True)  # Field name made lowercase.
    purchdate = models.CharField(db_column='PurchDate', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qideallev = models.IntegerField(db_column='QIdealLev', blank=True, null=True)  # Field name made lowercase.
    ppu = models.FloatField(db_column='PPU', blank=True, null=True)  # Field name made lowercase.
    qstart = models.IntegerField(db_column='Qstart', blank=True, null=True)  # Field name made lowercase.
    discrep = models.CharField(db_column='Discrep', max_length=200, blank=True, null=True)  # Field name made lowercase.
    discrepq = models.FloatField(db_column='DiscrepQ', blank=True, null=True)  # Field name made lowercase.
    comntdiscrep = models.CharField(db_column='ComntDiscrep', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qtytotsales = models.FloatField(db_column='QtyTotSales', blank=True, null=True)  # Field name made lowercase.
    picturecode = models.IntegerField(db_column='PictureCode', blank=True, null=True)  # Field name made lowercase.
    accompany = models.CharField(db_column='Accompany', max_length=200, blank=True, null=True)  # Field name made lowercase.
    descrip = models.CharField(db_column='Descrip', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stockable = models.CharField(db_column='Stockable', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qtystore = models.IntegerField(db_column='QtyStore', blank=True, null=True)  # Field name made lowercase.
    nametake = models.CharField(db_column='NameTake', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qadded = models.FloatField(db_column='Qadded', blank=True, null=True)  # Field name made lowercase.
    qsold = models.FloatField(db_column='Qsold', blank=True, null=True)  # Field name made lowercase.
    qpending = models.FloatField(db_column='Qpending', blank=True, null=True)  # Field name made lowercase.
    qbal = models.FloatField(db_column='Qbal', blank=True, null=True)  # Field name made lowercase.
    buttoncode = models.IntegerField(db_column='ButtonCode', blank=True, null=True)  # Field name made lowercase.
    spoilages = models.FloatField(db_column='Spoilages', blank=True, null=True)  # Field name made lowercase.
    bom = models.FloatField(db_column='BOM', blank=True, null=True)  # Field name made lowercase.
    phybal = models.FloatField(db_column='PhyBal', blank=True, null=True)  # Field name made lowercase.
    itemsource = models.CharField(db_column='ItemSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=200, blank=True, null=True)  # Field name made lowercase.
    costcode = models.CharField(db_column='CostCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.IntegerField(db_column='Taxtype', blank=True, null=True)  # Field name made lowercase.
    disctype = models.IntegerField(db_column='DiscType', blank=True, null=True)  # Field name made lowercase.
    discperc = models.FloatField(db_column='DiscPerc', blank=True, null=True)  # Field name made lowercase.
    storetype = models.CharField(db_column='StoreType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    multistore = models.CharField(db_column='MultiStore', max_length=200, blank=True, null=True)  # Field name made lowercase.
    editsale = models.CharField(db_column='EditSale', max_length=200, blank=True, null=True)  # Field name made lowercase.
    salescom = models.FloatField(db_column='SalesCom', blank=True, null=True)  # Field name made lowercase.
    deleted = models.CharField(db_column='Deleted', max_length=200, blank=True, null=True)  # Field name made lowercase.
    convtocode = models.FloatField(db_column='ConvToCode', blank=True, null=True)  # Field name made lowercase.
    convvalue = models.FloatField(db_column='ConvValue', blank=True, null=True)  # Field name made lowercase.
    ppu1 = models.FloatField(db_column='PPU1', blank=True, null=True)  # Field name made lowercase.
    ppu2 = models.FloatField(db_column='PPU2', blank=True, null=True)  # Field name made lowercase.
    ppu3 = models.FloatField(db_column='PPU3', blank=True, null=True)  # Field name made lowercase.
    ppu4 = models.FloatField(db_column='PPU4', blank=True, null=True)  # Field name made lowercase.
    ppu5 = models.FloatField(db_column='PPU5', blank=True, null=True)  # Field name made lowercase.
    selfservice = models.CharField(db_column='SelfService', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemdesc = models.CharField(db_column='ItemDesc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    quickmenu = models.CharField(db_column='QuickMenu', max_length=200, blank=True, null=True)  # Field name made lowercase.
    periodcount = models.FloatField(db_column='PeriodCount', blank=True, null=True)  # Field name made lowercase.
    periodsales = models.FloatField(db_column='PeriodSales', blank=True, null=True)  # Field name made lowercase.
    monthlycount = models.FloatField(db_column='MonthlyCount', blank=True, null=True)  # Field name made lowercase.
    monthlysales = models.FloatField(db_column='MonthlySales', blank=True, null=True)  # Field name made lowercase.
    yearlycount = models.FloatField(db_column='YearlyCount', blank=True, null=True)  # Field name made lowercase.
    yearlysales = models.FloatField(db_column='YearlySales', blank=True, null=True)  # Field name made lowercase.
    periodperc = models.FloatField(db_column='PeriodPerc', blank=True, null=True)  # Field name made lowercase.
    monthlyperc = models.FloatField(db_column='MonthlyPerc', blank=True, null=True)  # Field name made lowercase.
    yearlyperc = models.FloatField(db_column='YearlyPerc', blank=True, null=True)  # Field name made lowercase.
    externalprice = models.FloatField(db_column='ExternalPrice', blank=True, null=True)  # Field name made lowercase.
    scannercode = models.CharField(db_column='ScannerCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    currprice1 = models.FloatField(db_column='CurrPrice1', blank=True, null=True)  # Field name made lowercase.
    currprice2 = models.FloatField(db_column='CurrPrice2', blank=True, null=True)  # Field name made lowercase.
    currprice3 = models.FloatField(db_column='CurrPrice3', blank=True, null=True)  # Field name made lowercase.
    currprice4 = models.FloatField(db_column='CurrPrice4', blank=True, null=True)  # Field name made lowercase.
    currprice5 = models.FloatField(db_column='CurrPrice5', blank=True, null=True)  # Field name made lowercase.
    reorderqty = models.FloatField(db_column='ReorderQty', blank=True, null=True)  # Field name made lowercase.
    sysbalbak = models.FloatField(db_column='SysBalBak', blank=True, null=True)  # Field name made lowercase.
    incomeacc = models.CharField(db_column='IncomeAcc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    irefnumid = models.CharField(db_column='iRefNumID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    multiprice = models.IntegerField(db_column='MultiPrice', blank=True, null=True)  # Field name made lowercase.
    icopied = models.IntegerField(db_column='iCopied', blank=True, null=True)  # Field name made lowercase.
    ipeek = models.CharField(db_column='iPeek', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sadfate = models.CharField(db_column='SadFate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    storename = models.CharField(db_column='StoreName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    trackportions = models.CharField(db_column='TrackPortions', max_length=200, blank=True, null=True)  # Field name made lowercase.
    icopied1 = models.IntegerField(db_column='iCopied1', blank=True, null=True)  # Field name made lowercase.
    minqty = models.FloatField(db_column='MinQty', blank=True, null=True)  # Field name made lowercase.
    mrqty = models.FloatField(db_column='MrQty', blank=True, null=True)  # Field name made lowercase.
    atzero = models.CharField(db_column='AtZero', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wholesaleprice = models.FloatField(db_column='wholeSalePrice', blank=True, null=True)  # Field name made lowercase.
    wholesaleqty = models.FloatField(db_column='wholeSaleQty', blank=True, null=True)  # Field name made lowercase.
    trackkitportions = models.CharField(db_column='TrackKitPortions', max_length=200, blank=True, null=True)  # Field name made lowercase.
    marginrangefrom = models.FloatField(db_column='MarginRangeFrom', blank=True, null=True)  # Field name made lowercase.
    marginrangeto = models.FloatField(db_column='MarginRangeTo', blank=True, null=True)  # Field name made lowercase.
    istockbalqty = models.FloatField(db_column='iStockBalQty', blank=True, null=True)  # Field name made lowercase.
    hscode = models.CharField(db_column='HsCode', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itemstab'


class Itemstocksumtbl(models.Model):
    itemcode = models.IntegerField(db_column='ItemCode', primary_key=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itemstocksumtbl'


class Ivardata(models.Model):
    itemcode = models.IntegerField(db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemgroup = models.CharField(db_column='ItemGroup', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemsource = models.CharField(db_column='ItemSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ppu = models.FloatField(db_column='PPU', blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    transdate = models.DateField(db_column='TransDate', blank=True, null=True)  # Field name made lowercase.
    opening = models.FloatField(db_column='Opening', blank=True, null=True)  # Field name made lowercase.
    added = models.FloatField(db_column='Added', blank=True, null=True)  # Field name made lowercase.
    sold = models.FloatField(db_column='Sold', blank=True, null=True)  # Field name made lowercase.
    spoilt = models.FloatField(db_column='Spoilt', blank=True, null=True)  # Field name made lowercase.
    sysbal = models.FloatField(db_column='SysBal', blank=True, null=True)  # Field name made lowercase.
    phybal = models.FloatField(db_column='PhyBal', blank=True, null=True)  # Field name made lowercase.
    ivariance = models.FloatField(db_column='iVariance', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.FloatField(db_column='UnitCost', blank=True, null=True)  # Field name made lowercase.
    autonum = models.AutoField(db_column='AutoNum', primary_key=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ivardata'


class Iwaiterpmodes(models.Model):
    itransno = models.AutoField(db_column='iTransNo', primary_key=True)  # Field name made lowercase.
    iwaitername = models.CharField(db_column='iWaiterName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ipaymodeid = models.IntegerField(db_column='iPaymodeId', blank=True, null=True)  # Field name made lowercase.
    ipaymodename = models.CharField(db_column='iPaymodeName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'iwaiterpmodes'


class Listcostcodestbl(models.Model):
    costcode = models.CharField(db_column='CostCode', primary_key=True, max_length=200)  # Field name made lowercase.
    costcodename = models.CharField(db_column='CostCodeName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'listcostcodestbl'


class Liststorestbl(models.Model):
    storecode = models.CharField(db_column='StoreCode', primary_key=True, max_length=200)  # Field name made lowercase.
    storename = models.CharField(db_column='StoreName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'liststorestbl'


class Logintab(models.Model):
    num = models.AutoField(db_column='Num', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logintab'


class Logintabdfd(models.Model):
    num = models.AutoField(db_column='Num', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logintabdfd'


class Monthlysalestbl(models.Model):
    shiftdate = models.DateField(db_column='ShiftDate', blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', primary_key=True)  # Field name made lowercase.
    shifttime = models.CharField(db_column='ShiftTime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cashiername = models.CharField(db_column='CashierName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cash = models.FloatField(db_column='CASH', blank=True, null=True)  # Field name made lowercase.
    credit = models.FloatField(db_column='CREDIT', blank=True, null=True)  # Field name made lowercase.
    vcard = models.FloatField(db_column='VCARD', blank=True, null=True)  # Field name made lowercase.
    cheque = models.FloatField(db_column='CHEQUE', blank=True, null=True)  # Field name made lowercase.
    package = models.FloatField(db_column='PACKAGE', blank=True, null=True)  # Field name made lowercase.
    office = models.FloatField(db_column='OFFICE', blank=True, null=True)  # Field name made lowercase.
    comple = models.FloatField(db_column='COMPLE', blank=True, null=True)  # Field name made lowercase.
    uncleared = models.FloatField(db_column='UNCLEARED', blank=True, null=True)  # Field name made lowercase.
    roomcash = models.FloatField(db_column='ROOMCASH', blank=True, null=True)  # Field name made lowercase.
    roomcred = models.FloatField(db_column='ROOMCRED', blank=True, null=True)  # Field name made lowercase.
    roomvcard = models.FloatField(db_column='ROOMVCARD', blank=True, null=True)  # Field name made lowercase.
    grosstot = models.FloatField(db_column='GROSSTOT', blank=True, null=True)  # Field name made lowercase.
    actualtot = models.FloatField(db_column='ACTUALTOT', blank=True, null=True)  # Field name made lowercase.
    overshort = models.FloatField(db_column='OVERSHORT', blank=True, null=True)  # Field name made lowercase.
    cashintill = models.FloatField(db_column='CashInTill', blank=True, null=True)  # Field name made lowercase.
    floatamount = models.FloatField(db_column='FloatAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'monthlysalestbl'


class Mpesatransactions(models.Model):
    trans_id = models.AutoField(db_column='trans_ID', primary_key=True)  # Field name made lowercase.
    trans_code = models.IntegerField(db_column='trans_Code', blank=True, null=True)  # Field name made lowercase.
    trans_refid = models.CharField(db_column='trans_RefID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    trans_date = models.DateField(db_column='trans_Date', blank=True, null=True)  # Field name made lowercase.
    trans_time = models.CharField(db_column='trans_Time', max_length=200, blank=True, null=True)  # Field name made lowercase.
    trans_amount = models.FloatField(db_column='trans_Amount', blank=True, null=True)  # Field name made lowercase.
    trans_phoneno = models.CharField(db_column='trans_phoneNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    trans_firstname = models.CharField(db_column='trans_FirstName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    trans_lastname = models.CharField(db_column='trans_LastName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    trans_status = models.CharField(db_column='trans_Status', max_length=200, blank=True, null=True)  # Field name made lowercase.
    trans_amtused = models.FloatField(db_column='trans_AmtUsed', blank=True, null=True)  # Field name made lowercase.
    trans_waitername = models.CharField(db_column='trans_WaiterName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    module = models.CharField(max_length=200, blank=True, null=True)
    billnumber = models.CharField(db_column='billNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cashier = models.CharField(max_length=200, blank=True, null=True)
    mpesamessage = models.CharField(db_column='MpesaMessage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    salepoint = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mpesatransactions'


class Paymenttbl(models.Model):
    transno = models.AutoField(db_column='TransNo', primary_key=True)  # Field name made lowercase.
    billno = models.IntegerField(db_column='BillNo', blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=200, blank=True, null=True)  # Field name made lowercase.
    curramt = models.FloatField(db_column='CurrAmt', blank=True, null=True)  # Field name made lowercase.
    currrate = models.FloatField(db_column='CurrRate', blank=True, null=True)  # Field name made lowercase.
    baseamount = models.FloatField(db_column='BaseAmount', blank=True, null=True)  # Field name made lowercase.
    paymode = models.CharField(db_column='PayMode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paytime = models.DateTimeField(db_column='PayTime', blank=True, null=True)  # Field name made lowercase.
    paydate = models.DateField(db_column='PayDate', blank=True, null=True)  # Field name made lowercase.
    serviceperiod = models.CharField(db_column='ServicePeriod', max_length=200, blank=True, null=True)  # Field name made lowercase.
    waiter = models.CharField(db_column='Waiter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paymenttbl'


class Paymodestbl(models.Model):
    num = models.AutoField(db_column='Num', primary_key=True)  # Field name made lowercase.
    paymode = models.CharField(db_column='Paymode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paytype = models.IntegerField(db_column='PayType', blank=True, null=True)  # Field name made lowercase.
    visiblestatus = models.CharField(db_column='VisibleStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    zeroatclear = models.CharField(db_column='ZeroAtClear', max_length=200, blank=True, null=True)  # Field name made lowercase.
    setdefault = models.CharField(db_column='SetDefault', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paymodestbl'


class Payouttbl(models.Model):
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    transdate = models.DateField(db_column='TransDate', blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    systemtime = models.CharField(db_column='SystemTime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paidto = models.CharField(db_column='PaidTo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grn_amount = models.FloatField(blank=True, null=True)
    grnno = models.IntegerField(blank=True, null=True)
    grncomment = models.CharField(max_length=200, blank=True, null=True)
    supplier = models.CharField(max_length=200, blank=True, null=True)
    runningbal = models.FloatField(db_column='RunningBal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payouttbl'


class Portionsdeleted(models.Model):
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    itemcoderest = models.IntegerField(db_column='ItemCodeRest', blank=True, null=True)  # Field name made lowercase.
    itemnamerest = models.CharField(db_column='ItemNameRest', max_length=200, blank=True, null=True)  # Field name made lowercase.
    unitsrest = models.CharField(db_column='UnitsRest', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ppurest = models.FloatField(db_column='PPUrest', blank=True, null=True)  # Field name made lowercase.
    itemsource = models.CharField(db_column='ItemSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    ucost = models.FloatField(db_column='Ucost', blank=True, null=True)  # Field name made lowercase.
    qrestsoldb4 = models.FloatField(db_column='QrestSoldB4', blank=True, null=True)  # Field name made lowercase.
    qrestsold = models.FloatField(db_column='QrestSold', blank=True, null=True)  # Field name made lowercase.
    qstoreaddedb4 = models.FloatField(db_column='QstoreAddedB4', blank=True, null=True)  # Field name made lowercase.
    qstoreadded = models.FloatField(db_column='QstoreAdded', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'portionsdeleted'


class Posaudittrans(models.Model):
    tdate = models.CharField(db_column='Tdate', max_length=600, blank=True, null=True)  # Field name made lowercase.
    ttime = models.CharField(db_column='Ttime', max_length=600, blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=600, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=600, blank=True, null=True)  # Field name made lowercase.
    nature = models.CharField(db_column='Nature', max_length=600, blank=True, null=True)  # Field name made lowercase.
    descrip = models.CharField(db_column='Descrip', max_length=1500, blank=True, null=True)  # Field name made lowercase.
    state1 = models.CharField(db_column='State1', max_length=600, blank=True, null=True)  # Field name made lowercase.
    state2 = models.CharField(db_column='State2', max_length=600, blank=True, null=True)  # Field name made lowercase.
    auto = models.IntegerField(db_column='Auto', blank=True, null=True)  # Field name made lowercase.
    imodulename = models.CharField(db_column='iModuleName', max_length=600, blank=True, null=True)  # Field name made lowercase.
    priority = models.CharField(db_column='Priority', max_length=600, blank=True, null=True)  # Field name made lowercase.
    ifunction = models.CharField(db_column='iFunction', max_length=600, blank=True, null=True)  # Field name made lowercase.
    ireleasenum = models.CharField(db_column='iReleaseNum', max_length=600, blank=True, null=True)  # Field name made lowercase.
    insynch = models.CharField(db_column='inSynch', max_length=600, blank=True, null=True)  # Field name made lowercase.
    pc_date = models.CharField(max_length=200, blank=True, null=True)
    loggeduser = models.CharField(max_length=200, blank=True, null=True)
    refno = models.AutoField(db_column='RefNo', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'posaudittrans'


class Printmanager(models.Model):
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    printername = models.CharField(db_column='PrinterName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=200, blank=True, null=True)  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    waiter = models.CharField(db_column='Waiter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tableno = models.CharField(db_column='TableNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibdate = models.DateField(db_column='IBdate', blank=True, null=True)  # Field name made lowercase.
    ibtime = models.CharField(db_column='IBtime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    timesent = models.CharField(db_column='TimeSent', max_length=200, blank=True, null=True)  # Field name made lowercase.
    timeprinted = models.CharField(db_column='TimePrinted', max_length=200, blank=True, null=True)  # Field name made lowercase.
    printstatus = models.CharField(db_column='PrintStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'printmanager'


class Printsettings(models.Model):
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    printtype = models.CharField(db_column='PrintType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    printercomp = models.CharField(db_column='PrinterComp', max_length=200, blank=True, null=True)  # Field name made lowercase.
    printername = models.CharField(db_column='PrinterName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    printoption = models.CharField(db_column='PrintOption', max_length=200, blank=True, null=True)  # Field name made lowercase.
    printerstatus = models.CharField(db_column='PrinterStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    papersize = models.CharField(db_column='PaperSize', max_length=200, blank=True, null=True)  # Field name made lowercase.
    printpreview = models.CharField(db_column='PrintPreview', max_length=200, blank=True, null=True)  # Field name made lowercase.
    copies = models.IntegerField(db_column='Copies', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'printsettings'


class Printsettingsnew(models.Model):
    printid = models.AutoField(db_column='PrintID', primary_key=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='WorkStation', max_length=200)  # Field name made lowercase.
    itemsource = models.CharField(db_column='ItemSource', max_length=200)  # Field name made lowercase.
    printstation = models.CharField(db_column='PrintStation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    printdoc = models.CharField(db_column='PrintDoc', max_length=200)  # Field name made lowercase.
    printername = models.CharField(db_column='PrinterName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    printerstatus = models.CharField(db_column='PrinterStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    papersize = models.CharField(db_column='PaperSize', max_length=200, blank=True, null=True)  # Field name made lowercase.
    printpreview = models.CharField(db_column='PrintPreview', max_length=200, blank=True, null=True)  # Field name made lowercase.
    copies = models.IntegerField(db_column='Copies', blank=True, null=True)  # Field name made lowercase.
    transtype = models.CharField(db_column='TransType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'printsettingsnew'
        unique_together = (('printid', 'workstation', 'itemsource', 'printdoc'),)


class Removedtab(models.Model):
    iblno = models.CharField(db_column='IBLno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tbno = models.CharField(db_column='TBno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wtname = models.CharField(db_column='WTname', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibtime = models.CharField(db_column='IBtime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qnty = models.IntegerField(db_column='Qnty', blank=True, null=True)  # Field name made lowercase.
    ppu = models.FloatField(db_column='PPU', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibdate = models.DateField(db_column='IBdate', blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    postedby = models.CharField(db_column='PostedBy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    guestname = models.CharField(db_column='GuestName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    workstationname = models.CharField(db_column='WorkstationName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    refsauto = models.IntegerField(db_column='RefSAuto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'removedtab'


class Revertedtbl(models.Model):
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    billno = models.IntegerField(db_column='BillNo', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billtime = models.CharField(db_column='BillTime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paymode = models.CharField(db_column='PayMode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    waiter = models.CharField(db_column='Waiter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cashier = models.CharField(db_column='Cashier', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftno = models.CharField(db_column='ShiftNo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'revertedtbl'


class Roomchargetab(models.Model):
    iblno = models.IntegerField(db_column='IBLno', blank=True, null=True)  # Field name made lowercase.
    waiter = models.CharField(db_column='Waiter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    times = models.CharField(db_column='TimeS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    guestname = models.CharField(db_column='GuestName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    roomno = models.CharField(db_column='RoomNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accno = models.CharField(db_column='AccNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    charge = models.FloatField(db_column='Charge', blank=True, null=True)  # Field name made lowercase.
    paymode = models.CharField(db_column='PayMode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billtime = models.CharField(db_column='BillTime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftnox = models.CharField(db_column='ShiftNoX', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roomchargetab'


class Salepointsources(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sourcename = models.CharField(db_column='SourceName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    salepointid = models.IntegerField(db_column='SalePointId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salepointsources'


class Salepointstbl(models.Model):
    xbarcode = models.FloatField(db_column='xBarCode', blank=True, null=True)  # Field name made lowercase.
    xbarname = models.CharField(db_column='xBarName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stocktakedone = models.CharField(db_column='StockTakeDone', max_length=200, blank=True, null=True)  # Field name made lowercase.
    priceid = models.IntegerField(db_column='PriceId', blank=True, null=True)  # Field name made lowercase.
    rev_centername = models.CharField(db_column='Rev_CenterName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    billmessage = models.CharField(db_column='BillMessage', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mustsendorder = models.CharField(db_column='MustSendOrder', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salepointstbl'


class Salepointtransfer(models.Model):
    transcode = models.AutoField(db_column='TransCode', primary_key=True)  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sourcecat = models.CharField(db_column='SourceCat', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sourcepoint = models.CharField(db_column='SourcePoint', max_length=200, blank=True, null=True)  # Field name made lowercase.
    transferqty = models.FloatField(db_column='TransferQty', blank=True, null=True)  # Field name made lowercase.
    destinationpoint = models.CharField(db_column='DestinationPoint', max_length=200, blank=True, null=True)  # Field name made lowercase.
    transdate = models.DateField(db_column='TransDate', blank=True, null=True)  # Field name made lowercase.
    transferby = models.CharField(db_column='TransferBy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    transtime = models.CharField(db_column='TransTime', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salepointtransfer'


class Serviceperiods(models.Model):
    periodid = models.AutoField(db_column='PeriodId', primary_key=True)  # Field name made lowercase.
    periodstarttime = models.TimeField(db_column='PeriodStartTime', blank=True, null=True)  # Field name made lowercase.
    periodendtime = models.TimeField(db_column='PeriodEndTime', blank=True, null=True)  # Field name made lowercase.
    perioddesc = models.CharField(db_column='PeriodDesc', max_length=600, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serviceperiods'


class Serviceperview(models.Model):
    perid = models.AutoField(db_column='perID', primary_key=True)  # Field name made lowercase.
    serviceperiod = models.CharField(db_column='ServicePeriod', max_length=200, blank=True, null=True)  # Field name made lowercase.
    postto = models.CharField(max_length=200, blank=True, null=True)
    totalsales = models.FloatField(db_column='TotalSales', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serviceperview'


class Shiftbackuptab(models.Model):
    shiftnum = models.CharField(db_column='ShiftNum', primary_key=True, max_length=200)  # Field name made lowercase.
    sdate = models.DateField(db_column='SDate', blank=True, null=True)  # Field name made lowercase.
    cash = models.FloatField(db_column='Cash', blank=True, null=True)  # Field name made lowercase.
    credit = models.FloatField(db_column='Credit', blank=True, null=True)  # Field name made lowercase.
    vcard = models.FloatField(db_column='VCard', blank=True, null=True)  # Field name made lowercase.
    comple = models.FloatField(db_column='Comple', blank=True, null=True)  # Field name made lowercase.
    house = models.FloatField(db_column='House', blank=True, null=True)  # Field name made lowercase.
    wrongent = models.FloatField(db_column='WrongEnt', blank=True, null=True)  # Field name made lowercase.
    uncleared = models.FloatField(db_column='Uncleared', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shiftbackuptab'


class Signatorytable(models.Model):
    reportid = models.IntegerField(db_column='ReportId')  # Field name made lowercase.
    reportname = models.CharField(db_column='ReportName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    signatoryname = models.CharField(db_column='SignatoryName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'signatorytable'


class Signatorytbl(models.Model):
    reportid = models.IntegerField(db_column='ReportId', primary_key=True)  # Field name made lowercase.
    report = models.CharField(db_column='Report', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sig1 = models.CharField(db_column='Sig1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sig2 = models.CharField(db_column='Sig2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sig3 = models.CharField(db_column='Sig3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sig4 = models.CharField(db_column='Sig4', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'signatorytbl'


class SourceOrders(models.Model):
    orders_id = models.AutoField(db_column='orders_ID', primary_key=True)  # Field name made lowercase.
    orders_date = models.DateField(db_column='orders_Date', blank=True, null=True)  # Field name made lowercase.
    orders_billno = models.IntegerField(db_column='orders_BillNo', blank=True, null=True)  # Field name made lowercase.
    orders_waiter = models.CharField(db_column='orders_Waiter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    orders_source = models.CharField(db_column='orders_Source', max_length=200, blank=True, null=True)  # Field name made lowercase.
    orders_ready = models.IntegerField(db_column='orders_Ready', blank=True, null=True)  # Field name made lowercase.
    orders_served = models.IntegerField(db_column='orders_Served', blank=True, null=True)  # Field name made lowercase.
    orders_servedby = models.CharField(db_column='orders_ServedBy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    orders_ordernum = models.IntegerField(db_column='orders_OrderNum', blank=True, null=True)  # Field name made lowercase.
    orders_shiftnum = models.IntegerField(db_column='orders_ShiftNum', blank=True, null=True)  # Field name made lowercase.
    orders_tablenum = models.CharField(db_column='orders_TableNum', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'source_orders'


class Sourceexcluded(models.Model):
    excludeid = models.AutoField(db_column='ExcludeID', primary_key=True)  # Field name made lowercase.
    excludepcname = models.CharField(db_column='ExcludePCName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    excludesource = models.CharField(db_column='ExcludeSource', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sourceexcluded'


class Sourcegroups(models.Model):
    itemsource = models.CharField(db_column='ItemSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemgroup = models.CharField(db_column='ItemGroup', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sourcegroups'


class Sourcenew(models.Model):
    itemsource = models.CharField(db_column='ItemSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stocktakemust = models.CharField(db_column='StockTakeMust', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stocktakestatus = models.CharField(db_column='StockTakeStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stocktype = models.CharField(db_column='StockType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    orderprintstation = models.CharField(db_column='OrderPrintStation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    orderprintername = models.CharField(db_column='OrderPrinterName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ideci = models.FloatField(db_column='iDeci', blank=True, null=True)  # Field name made lowercase.
    isale = models.CharField(db_column='iSale', max_length=200, blank=True, null=True)  # Field name made lowercase.
    papersize = models.CharField(db_column='PaperSize', max_length=200, blank=True, null=True)  # Field name made lowercase.
    voidorder = models.CharField(db_column='VoidOrder', max_length=200, blank=True, null=True)  # Field name made lowercase.
    printpreview = models.CharField(db_column='PrintPreview', max_length=200, blank=True, null=True)  # Field name made lowercase.
    copies = models.IntegerField(db_column='Copies', blank=True, null=True)  # Field name made lowercase.
    sendorders = models.CharField(db_column='SendOrders', max_length=200, blank=True, null=True)  # Field name made lowercase.
    alternatestation = models.CharField(db_column='AlternateStation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    alternateprinter = models.CharField(db_column='AlternatePrinter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastorderno = models.FloatField(db_column='LastOrderNo', blank=True, null=True)  # Field name made lowercase.
    printerip = models.CharField(db_column='PrinterIP', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sourcenew'


class Stockaudittbl(models.Model):
    audit_id = models.AutoField(db_column='audit_Id', primary_key=True)  # Field name made lowercase.
    audit_billno = models.IntegerField(db_column='audit_BillNo', blank=True, null=True)  # Field name made lowercase.
    audit_ibsales = models.FloatField(blank=True, null=True)
    audit_materials = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stockaudittbl'


class Stocksadded(models.Model):
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemcat = models.CharField(db_column='ItemCat', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ucost = models.FloatField(db_column='Ucost', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=200, blank=True, null=True)  # Field name made lowercase.
    datetrans = models.DateField(db_column='DateTrans', blank=True, null=True)  # Field name made lowercase.
    timetrans = models.CharField(db_column='TimeTrans', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True, null=True)  # Field name made lowercase.
    postedby = models.CharField(db_column='postedBy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qusedb4 = models.FloatField(db_column='QusedB4', blank=True, null=True)  # Field name made lowercase.
    qaddedb4 = models.FloatField(db_column='QaddedB4', blank=True, null=True)  # Field name made lowercase.
    qused = models.FloatField(db_column='Qused', blank=True, null=True)  # Field name made lowercase.
    qadded = models.FloatField(db_column='Qadded', blank=True, null=True)  # Field name made lowercase.
    spoilages = models.FloatField(db_column='Spoilages', blank=True, null=True)  # Field name made lowercase.
    phybal = models.FloatField(db_column='PhyBal', blank=True, null=True)  # Field name made lowercase.
    convcodevalue = models.CharField(db_column='ConvCodeValue', max_length=200, blank=True, null=True)  # Field name made lowercase.
    barcode = models.FloatField(db_column='BarCode', blank=True, null=True)  # Field name made lowercase.
    itemsource = models.CharField(db_column='ItemSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lbp_pos = models.CharField(db_column='LBP_POS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lbw_id = models.CharField(db_column='LBW_ID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stockbalyes = models.CharField(db_column='StockBalYes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    posttime = models.DateTimeField(db_column='PostTime')  # Field name made lowercase.
    transtype = models.CharField(db_column='TransType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prodgrp = models.CharField(db_column='ProdGrp', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stocksadded'


class Stocksaddedmanual(models.Model):
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemcat = models.CharField(db_column='ItemCat', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    ucost = models.FloatField(db_column='Ucost', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=200, blank=True, null=True)  # Field name made lowercase.
    datetrans = models.DateField(db_column='DateTrans', blank=True, null=True)  # Field name made lowercase.
    timetrans = models.CharField(db_column='TimeTrans', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True, null=True)  # Field name made lowercase.
    postedby = models.CharField(db_column='postedBy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qusedb4 = models.FloatField(db_column='QusedB4', blank=True, null=True)  # Field name made lowercase.
    qaddedb4 = models.FloatField(db_column='QaddedB4', blank=True, null=True)  # Field name made lowercase.
    qused = models.FloatField(db_column='Qused', blank=True, null=True)  # Field name made lowercase.
    qadded = models.FloatField(db_column='Qadded', blank=True, null=True)  # Field name made lowercase.
    spoilages = models.FloatField(db_column='Spoilages', blank=True, null=True)  # Field name made lowercase.
    phybal = models.FloatField(db_column='PhyBal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stocksaddedmanual'


class Stocksettingstbl(models.Model):
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.
    dept = models.CharField(db_column='Dept', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stocksetting = models.CharField(db_column='StockSetting', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stocktaking = models.CharField(db_column='StockTaking', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stocksettingstbl'


class Tablersv(models.Model):
    transid = models.AutoField(db_column='TransId', primary_key=True)  # Field name made lowercase.
    tableno = models.CharField(db_column='TableNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reservedfor = models.CharField(db_column='ReservedFor', max_length=200, blank=True, null=True)  # Field name made lowercase.
    resdate = models.DateField(db_column='ResDate', blank=True, null=True)  # Field name made lowercase.
    starttime = models.TimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.TimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    covers = models.FloatField(db_column='Covers', blank=True, null=True)  # Field name made lowercase.
    reservedby = models.CharField(db_column='ReservedBy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reservedate = models.DateField(db_column='ReserveDate', blank=True, null=True)  # Field name made lowercase.
    servedby = models.CharField(db_column='ServedBy', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tablersv'


class Tablestab(models.Model):
    tbcode = models.AutoField(db_column='TbCode', primary_key=True)  # Field name made lowercase.
    tbno = models.CharField(db_column='TBno', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tablestab'


class Tempitemscopy(models.Model):
    transno = models.AutoField(db_column='TransNo', primary_key=True)  # Field name made lowercase.
    billno = models.IntegerField(db_column='BillNo', blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=200, blank=True, null=True)  # Field name made lowercase.
    curramt = models.FloatField(db_column='CurrAmt', blank=True, null=True)  # Field name made lowercase.
    currrate = models.FloatField(db_column='CurrRate', blank=True, null=True)  # Field name made lowercase.
    baseamount = models.FloatField(db_column='BaseAmount', blank=True, null=True)  # Field name made lowercase.
    paymode = models.CharField(db_column='PayMode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paytime = models.DateTimeField(db_column='PayTime', blank=True, null=True)  # Field name made lowercase.
    paydate = models.DateField(db_column='PayDate', blank=True, null=True)  # Field name made lowercase.
    serviceperiod = models.CharField(db_column='ServicePeriod', max_length=200, blank=True, null=True)  # Field name made lowercase.
    waiter = models.CharField(db_column='Waiter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempitemscopy'


class Temptrackitems(models.Model):
    itemcode1 = models.IntegerField(db_column='Itemcode1', blank=True, null=True)  # Field name made lowercase.
    itemname1 = models.CharField(db_column='ItemName1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty1 = models.FloatField(db_column='Qty1', blank=True, null=True)  # Field name made lowercase.
    ppu1 = models.FloatField(db_column='PPU1', blank=True, null=True)  # Field name made lowercase.
    prodgrp1 = models.CharField(db_column='ProdGrp1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sourcecat1 = models.CharField(db_column='Sourcecat1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibdate1 = models.DateField(db_column='Ibdate1', blank=True, null=True)  # Field name made lowercase.
    ibdatetime = models.DateTimeField(db_column='IbdateTime', blank=True, null=True)  # Field name made lowercase.
    paymode1 = models.CharField(db_column='Paymode1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    datetrans1 = models.DateField(blank=True, null=True)
    transtype1 = models.CharField(max_length=200, blank=True, null=True)
    units1 = models.CharField(max_length=200, blank=True, null=True)
    qadded1 = models.FloatField(db_column='Qadded1', blank=True, null=True)  # Field name made lowercase.
    qsold1 = models.FloatField(db_column='Qsold1', blank=True, null=True)  # Field name made lowercase.
    postedby1 = models.CharField(db_column='Postedby1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qbal1 = models.FloatField(db_column='Qbal1', blank=True, null=True)  # Field name made lowercase.
    auto1 = models.AutoField(db_column='Auto1', primary_key=True)  # Field name made lowercase.
    ordernum = models.IntegerField(db_column='OrderNum', blank=True, null=True)  # Field name made lowercase.
    accum1 = models.FloatField(db_column='Accum1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temptrackitems'


class Ticketstbl(models.Model):
    transno = models.AutoField(db_column='TransNo', primary_key=True)  # Field name made lowercase.
    ticketno = models.IntegerField(db_column='TicketNo', blank=True, null=True)  # Field name made lowercase.
    ticketdate = models.DateField(db_column='TicketDate', blank=True, null=True)  # Field name made lowercase.
    tickettime = models.CharField(db_column='TicketTime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    barcode = models.IntegerField(db_column='BarCode', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    serialnum = models.IntegerField(db_column='SerialNum', blank=True, null=True)  # Field name made lowercase.
    pcname = models.CharField(db_column='PcName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ticketstbl'


class Tipstable(models.Model):
    transno = models.AutoField(db_column='TransNo', primary_key=True)  # Field name made lowercase.
    billno = models.IntegerField(db_column='BillNo', blank=True, null=True)  # Field name made lowercase.
    tableno = models.CharField(db_column='TableNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    waitername = models.CharField(db_column='WaiterName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cashiername = models.CharField(db_column='CashierName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    billamount = models.FloatField(db_column='BillAmount', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    tipamount = models.FloatField(db_column='TipAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipstable'


class Translogtbl(models.Model):
    tdate = models.DateField(db_column='Tdate', blank=True, null=True)  # Field name made lowercase.
    ttime = models.CharField(db_column='Ttime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nature = models.CharField(db_column='Nature', max_length=200, blank=True, null=True)  # Field name made lowercase.
    state1 = models.CharField(db_column='State1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    state2 = models.CharField(db_column='State2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    auto = models.AutoField(db_column='Auto', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'translogtbl'


class Voideditemslist(models.Model):
    sautonum = models.AutoField(db_column='SautoNum', primary_key=True)  # Field name made lowercase.
    iblno = models.IntegerField(db_column='IBLno', blank=True, null=True)  # Field name made lowercase.
    tbno = models.CharField(db_column='TBno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    waiter = models.CharField(db_column='Waiter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibtime = models.CharField(db_column='IBtime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibdate = models.DateField(db_column='IBdate', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ittime = models.CharField(db_column='ITtime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qnty = models.IntegerField(db_column='Qnty', blank=True, null=True)  # Field name made lowercase.
    ppu = models.FloatField(db_column='PPU', blank=True, null=True)  # Field name made lowercase.
    prodgrp = models.CharField(db_column='ProdGrp', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wrent = models.CharField(db_column='WrEnt', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sourcecat = models.CharField(db_column='SourceCat', max_length=200, blank=True, null=True)  # Field name made lowercase.
    postto = models.CharField(db_column='PostTo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    guestname = models.CharField(db_column='GuestName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    roomnum = models.CharField(db_column='RoomNum', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paymode = models.CharField(db_column='Paymode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shiftno = models.IntegerField(db_column='ShiftNo', blank=True, null=True)  # Field name made lowercase.
    ordered = models.CharField(db_column='Ordered', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemsource = models.CharField(db_column='ItemSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    storecode = models.CharField(db_column='StoreCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    costcode = models.CharField(db_column='CostCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    unitcost = models.FloatField(db_column='UnitCost', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=200, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.IntegerField(db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    disctype = models.IntegerField(db_column='DiscType', blank=True, null=True)  # Field name made lowercase.
    discperc = models.FloatField(db_column='DiscPerc', blank=True, null=True)  # Field name made lowercase.
    storetype = models.CharField(db_column='StoreType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accperiod = models.IntegerField(db_column='AccPeriod', blank=True, null=True)  # Field name made lowercase.
    iresttxnid = models.CharField(db_column='iRestTxnID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ipaytxnid = models.CharField(db_column='iPayTxnID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    barcode = models.FloatField(db_column='BarCode', blank=True, null=True)  # Field name made lowercase.
    exactqty = models.FloatField(db_column='ExactQty', blank=True, null=True)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idisctype = models.CharField(db_column='iDiscType', max_length=200)  # Field name made lowercase.
    discamt = models.FloatField(db_column='DiscAmt', blank=True, null=True)  # Field name made lowercase.
    aliasname = models.CharField(db_column='AliasName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ishappyhour = models.CharField(db_column='isHappyHour', max_length=200, blank=True, null=True)  # Field name made lowercase.
    serviceperiod = models.CharField(db_column='ServicePeriod', max_length=200, blank=True, null=True)  # Field name made lowercase.
    servicetime = models.DateTimeField(db_column='ServiceTime', blank=True, null=True)  # Field name made lowercase.
    taxa = models.FloatField(db_column='TaxA', blank=True, null=True)  # Field name made lowercase.
    taxb = models.FloatField(db_column='TaxB', blank=True, null=True)  # Field name made lowercase.
    taxc = models.FloatField(db_column='TaxC', blank=True, null=True)  # Field name made lowercase.
    taxamount = models.FloatField(db_column='TaxAmount', blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ordernum = models.FloatField(db_column='OrderNum', blank=True, null=True)  # Field name made lowercase.
    tempppu = models.FloatField(db_column='TempPPU', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'voideditemslist'


class Voidreasons(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    voidreason = models.CharField(db_column='VoidReason', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'voidreasons'


class Waitersinouttbl(models.Model):
    signid = models.AutoField(db_column='SignID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entrytype = models.CharField(db_column='EntryType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entrytime = models.CharField(db_column='EntryTime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entrydate = models.DateField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'waitersinouttbl'


class Waitertab(models.Model):
    wtno = models.AutoField(db_column='WTno', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idnum = models.CharField(db_column='IDnum', max_length=200, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    dateofdep = models.DateField(db_column='DateOfDep', blank=True, null=True)  # Field name made lowercase.
    passwd = models.CharField(db_column='Passwd', max_length=200, blank=True, null=True)  # Field name made lowercase.
    allowall = models.CharField(db_column='AllowAll', max_length=200, blank=True, null=True)  # Field name made lowercase.
    printorder = models.CharField(db_column='PrintOrder', max_length=200, blank=True, null=True)  # Field name made lowercase.
    printbill = models.CharField(db_column='PrintBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    clearbill = models.CharField(db_column='ClearBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    voidbill = models.CharField(db_column='VoidBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mergebill = models.CharField(db_column='MergeBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    splitbill = models.CharField(db_column='SplitBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    editbill = models.CharField(db_column='EditBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cardno = models.IntegerField(db_column='CardNo', blank=True, null=True)  # Field name made lowercase.
    maxpending = models.FloatField(db_column='MaxPending', blank=True, null=True)  # Field name made lowercase.
    comperc = models.FloatField(db_column='ComPerc', blank=True, null=True)  # Field name made lowercase.
    numofbills = models.IntegerField(db_column='NumOfBills', blank=True, null=True)  # Field name made lowercase.
    addtoprinted = models.CharField(db_column='AddToPrinted', max_length=200, blank=True, null=True)  # Field name made lowercase.
    barcode = models.FloatField(db_column='BarCode', blank=True, null=True)  # Field name made lowercase.
    allowaddall = models.CharField(db_column='AllowAddAll', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accessfunctions = models.CharField(db_column='AccessFunctions', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accessdiscounts = models.CharField(db_column='AccessDiscounts', max_length=200, blank=True, null=True)  # Field name made lowercase.
    inoutstatus = models.CharField(db_column='InOutStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    inouttime = models.CharField(db_column='InOutTime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accesscreatebill = models.CharField(db_column='AccessCreateBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accessinterim = models.CharField(db_column='AccessInterim', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accessorderstatus = models.CharField(db_column='AccessOrderStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    selwaiters = models.CharField(db_column='SelWaiters', max_length=200, blank=True, null=True)  # Field name made lowercase.
    switchspoints = models.CharField(db_column='SwitchSPoints', max_length=200, blank=True, null=True)  # Field name made lowercase.
    minimumsales = models.FloatField(db_column='MinimumSales', blank=True, null=True)  # Field name made lowercase.
    switchcurr = models.CharField(db_column='SwitchCurr', max_length=200, blank=True, null=True)  # Field name made lowercase.
    activestatus = models.CharField(db_column='ActiveStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    seeitembal = models.CharField(db_column='SeeItemBal', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(max_length=200, blank=True, null=True)
    allowcancel = models.CharField(db_column='AllowCancel', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastactive = models.CharField(db_column='LastActive', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ordermessage = models.CharField(db_column='OrderMessage', max_length=200, blank=True, null=True)  # Field name made lowercase.
    revertbill = models.CharField(db_column='RevertBill', max_length=200, blank=True, null=True)  # Field name made lowercase.
    openkey = models.CharField(db_column='OpenKey', max_length=20, blank=True, null=True)  # Field name made lowercase.
    allowexitbutton = models.CharField(db_column='AllowExitButton', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'waitertab'


class Wrongentrytab(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    iblno = models.CharField(db_column='IBLno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wtno = models.CharField(db_column='WTno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tbno = models.CharField(db_column='TBno', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ibdate = models.DateField(db_column='IBdate', blank=True, null=True)  # Field name made lowercase.
    ibtime = models.CharField(db_column='IBtime', max_length=200, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wrongentrytab'
