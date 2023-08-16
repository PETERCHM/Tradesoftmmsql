from django.db import models


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
