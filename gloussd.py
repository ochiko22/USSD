
def dataPlan():
    daplanTrans = input(
        "1. Proceed(Auto Renew)\n"
        "2. Proceed(On - Off)\n"
        "0. Back\n"
    )
    if daplanTrans == "1":
        # Buy Data Plans
        autorenew()
    elif daplanTrans == "2":
        # Match day spec
        oneoff()
    elif daplanTrans == "0":
        # Match day spec
        data()

    else:
        print(
            "Invalid Transaction Entry\n"
            "Try Again"
        )
        dataPlan()


# Blackberry
def blackberry():
    bB = input(
        'All Glo BB10 data Plans are now 3G-4G compatible\n'
        '1. Buy 3G-4G data\n'
        '2. Manage\n'
        '3. Back\n'
        '0. Exit\n'
    )
    if bB == "1":
        blackberryPlans()
    elif bB == "2":
        manageBlackberry()
    elif bB == "3":
        data()
    elif bB == "0":
        print("Glo Unlimited")
    else:
        print("Wrong code")
        blackberry()


# 3G TO 4G BLACKBERRY PLANS
def blackberryPlans():
    bBP = input(
        "1. BB 10 Plans\n"
        "2. Non BB 10 Plans\n"
        "0. Back\n"
    )
    if bBP == "1":
        bbTenPlans()
    elif bBP == "2":
        print("Blackberry services on your BBOS7 devices are no\n"
              "longer available. To know more visit\n"
              "www.gloworld.com/bb\n")
    elif bBP == "0":
        blackberry()


# bb10 plans
def bbTenPlans():
    bbTP = input(
        "These plans are for new customers & for renewals:\n"
        "1. #1000 = 1.8GB 30 Days\n"
        "2. #2000 = 4.5GB 30 Days\n"
        "3. #2500 = 7.2Gb 30 Days\n"
        "4. Back\n"
    )
    if bbTP == "1":
        print('You have been credited with #1000 valid for 30 days')
    elif bbTP == "2":
        print("You have been credited with #2000 valid for 30 days")
    elif bbTP == "3":
        print("You have been credited with #2500 valid for 30 days")
    elif bbTP == "4":
        blackberryPlans()


# MANAGE BLACKBERRY PLANS
def manageBlackberry():
    mBB = input(
        "Please select a choice\n"
        "1. APN Details\n"
        "2. Manage through Selfcare Portal\n"
        "3. Get Data Balance\n"
        "0. Back\n"
    )
    if mBB == "1":
        apnDetails()
    elif mBB == "2":
        print("http://bb.glo.com")
    elif mBB == "3":
        print("Error communicating with SME")
    elif mBB == "0":
        blackberry()
    else:
        print("Wrong code")
        manageBlackberry()


# APN DETAILS
def apnDetails():
    apnD = input(
        "The following settings should be on your phone\n"
        "1. Advanced system setting/TCPIP\n"
        "(For Non-BB 10 Devices only)\n"
        "APN Name: blackberry.net\n"
        "Username:\n"
        "Password:\n"
        "\n"
        "2. Settings/Mobile Network\n"
        "(For BB10 devices only)\n"
        "APN Name: blackberry.net\n"
        "Username:\n"
        "Password:\n"
        "\n"
        "3. Back\n"
    )
    if apnD == "3":
        manageBlackberry()
    else:
        pass


# Manage Data Plan
def manageDataPlan():
    mDP = input(
        "Please Select\n"
        "1. To get Data Settings\n"
        "2. To see Details for manual Configuration\n"
        "3. To go to Selfcare Portal\n"
        "4. To get Data Balance\n"
        "5. To Check Sharing Members\n"
        "6. Back\n"
    )
    if mDP == "1":
        print("Please send the keyword <flat> to 1234")
    elif mDP == "2":
        print("Please input the details on your handset manually\n"
              "(which would be in your setting option) and save\n"
              "APN Name: Glo Flat\n"
              "Username: flat\n"
              "Password: flat\n")
    elif mDP == "3":
        print("hsi.glo.com")
    elif mDP == "4":
        print("You are on a #1000, expires 09/12/2022 13:05,\n"
              "Your data balance 1492MB, browsed for 275 Min\n"
              "renewal status ACCEPTED\n")
    elif mDP == "5":
        print("You do not have any number sharing your subscription")
    elif mDP == "6":
        data()
    else:
        print("Wrong Code, Please try again")


# Share DataPlan
def shareDataPlan():
    sDP = input(
        'Share data plan\n'
        '1. Share\n'
        '2. Unshare\n'
    )
    if sDP == "1":
        yu = input(
            'Please enter subscriber\'s number: \n'
        )
        print("You have successfully shared your data plan with", yu)
    elif sDP == "2":
        yu = input(
            'Please enter subscriber\'s number: \n'
        )
        print("You have successfully unshared your data plan with", yu)
    else:
        shareDataPlan()


# giftdataplan
# specialdataoffer under gift
def specialDataoffer2():
    sDO2 = input(
        "1. Special Plans\n"
        "2. Campus Booster\n"
        "3. Back\n"
    )
    if sDO2 == "1":
        specialplans()
    elif sDO2 == "2":
        campusBooster()
    elif sDO2 == "3":
        giftDataPlan()
    else:
        print('Glo Unlimited')
        specialDataoffer2()


# socialbundles under gift
# instagrambundles under gift
def instagramBundles2():
    num = input(
        "Enter giftee number:\n"
    )
    if len(num) == 11 and num.isnumeric():
        print("Continue")
    else:
        print("Enter valid number")

    insta2 = input(
        "Instagram Bundles\n"
        "1. #25 = 20MB 1Day\n"
        "2. #50 = 50MB 7Days\n"
        "3. #100 = 125MB 30Days\n"
        "4. More Plans\n"
        "5. Back\n"
    )
    if insta2 == "1":
        print("You have credited with", num, "#25 valid for 1 Day")
    elif insta2 == "2":
        print("You have credited with", num, "#50 valid for 7 Days")
    elif insta2 == "3":
        print("You have credited with", num, "#100 valid for 30 Days")
    elif insta2 == "4":
        print("Glo Unlimited")
    elif insta2 == "5":
        singleBundles2()
    else:
        print("Wrong input, Please try again")
        instagramBundles2()


# telegrambundles
def telegramBundles2():
    num = input(
        "Enter giftee number:\n"
    )
    if len(num) == 11 and num.isnumeric():
        print("Continue")
    else:
        print("Enter valid number")

    telegram2 = input(
        "Telegram Bundles\n"
        "1. #25 = 20MB 1Day\n"
        "2. #50 = 50MB 7Days\n"
        "3. #100 = 125MB 30Days\n"
        "4. More Plans\n"
        "5. Back\n"
    )
    if telegram2 == "1":
        print("You have been credited", num, "with #25 valid for 1 Day")
    elif telegram2 == "2":
        print("You have been credited", num, "with #50 valid for 7 Days")
    elif telegram2 == "3":
        print("You have been credited", num, "with #100 valid for 30 Days")
    elif telegram2 == "4":
        instagramBundles2()
    elif telegram2 == "5":
        singleBundles2()
    else:
        print("Wrong input, Please try again")
        telegramBundles2()


# tiktokbundles
def tiktokBundles2():
    num = input(
        "Enter giftee number:\n"
    )
    if len(num) == 11 and num.isnumeric():
        print("Continue")
    else:
        print("Enter valid number")

    tiktok2 = input(
        "Tiktok Bundles\n"
        "1. #25 = 20MB 1Day\n"
        "2. #50 = 50MB 7Days\n"
        "3. #100 = 125MB 30Days\n"
        "4. More Plans\n"
        "5. Back\n"
    )
    if tiktok2 == "1":
        print("You have credited", num, "with #25 valid for 1 Day")
    elif tiktok2 == "2":
        print("You have credited", num, "with #50 valid for 7 Days")
    elif tiktok2 == "3":
        print("You have credited", num, "with #100 valid for 30 Days")
    elif tiktok2 == "4":
        telegramBundles2()
    elif tiktok2 == "5":
        singleBundles2()
    else:
        print("Wrong input, Please try again")
        tiktokBundles2()


# singlebundles under gift
def singleBundles2():
    singlebundle2 = input(
        "1. Tiktok\n"
        "2. Telegram\n"
        "3. Instagram\n"
        "4. Back\n"
    )
    if singlebundle2 == "1":
        tiktokBundles2()
    elif singlebundle2 == "2":
        telegramBundles2()
    elif singlebundle2 == "3":
        instagramBundles2()
    elif singlebundle2 == "4":
        socialbundles2()
    else:
        print("Wrong input, Please try again")
        singleBundles2()


# operabundles under gift
def operaBundles2():
    num = input(
        "Enter giftee number:\n"
    )
    if len(num) == 11 and num.isnumeric():
        print("Continue")
    else:
        print("Enter valid number")

    opBundles2 = input(
        "Opera Bundles\n"
        "1. #25 = 25MB 1Day\n"
        "2. #50 = 100MB 7Days\n"
        "3. #100 = 300MB 30Days\n"
        "4. More Plans\n"
        "5. Back\n"
    )
    if opBundles2 == "1":
        print("You have credited", num, "with #25 valid for 1 Day")
    elif opBundles2 == "2":
        print("You have credited", num, "with #50 valid for 7 Days")
    elif opBundles2 == "3":
        print("You have credited", num, "with #100 valid for 30 Days")
    elif opBundles2 == "4":
        singleBundles2()
    elif opBundles2 == "5":
        socialbundles2()
    else:
        print("Wrong input, Please try again")
        operaBundles2()


# youtubebundles under gift
def youtubeBundles2():
    num = input(
        "Enter giftee number:\n"
    )
    if len(num) == 11 and num.isnumeric():
        print("Continue")
    else:
        print("Enter valid number")

    ytBundles2 = input(
        "Youtube Bundles\n"
        "1. #50 = 100MB 1Day\n"
        "2. #50 = 1hour\n"
        "3. #50 = 5hours strasight\n"
        "4. #130 = 3hours\n"
        "5. #100 = 200MB 7Days\n"
        "6. #200 = 7hours night\n"
        "7. #250 = 500MB 30Days\n"
        "8. More Plans\n"
        "9. Back\n"
    )
    if ytBundles2 == "1":
        print("You have credited", num, "with #50 valid for 1 Day")
    elif ytBundles2 == "2":
        print("You have credited", num, "with #50 valid for 1 hour")
    elif ytBundles2 == "3":
        print("You have credited", num, "with #50 valid for 5 hours")
    elif ytBundles2 == "4":
        print("You have credited", num, "with #130 valid for 3 hours")
    elif ytBundles2 == "5":
        print("You have credited", num, "with #100 valid for 7 Days")
    elif ytBundles2 == "6":
        print("You have credited", num, "with #200 valid for 7 hours")
    elif ytBundles2 == "7":
        print("You have credited", num, "with #250 valid for 30 Days")
    elif ytBundles2 == "8":
        operaBundles2()
    elif ytBundles2 == "9":
        socialbundles2()
    else:
        print("Wrong input, Please try again")
        youtubeBundles2()


# WTFbundles
def wtfBundles2():
    num = input(
        "Enter giftee number:\n"
    )
    if len(num) == 11 and num.isnumeric():
        print("Continue")
    else:
        print("Enter valid number")

    wtfbundles2 = input(
        "Whatsapp + Twitter + Facebook Bundles\n"
        "1. #25 = 100MB 1Day\n"
        "2. #50 = 200MB 7Days\n"
        "3. #100 = 500MB 30Days\n"
        "4. More Plans\n"
        "5. Back\n"
    )
    if wtfbundles2 == "1":
        print("You have credited", num, "with #25 valid for 1 Day")
    elif wtfbundles2 == "2":
        print("You have credited", num, "with #50 valid for 7 Days")
    elif wtfbundles2 == "3":
        print("You have credited", num, "with #100 valid for 30 Days")
    elif wtfbundles2 == "4":
        youtubeBundles2()
    elif wtfbundles2 == "5":
        socialbundles2()
    else:
        print("Wrong input, Please try again")
        wtfBundles2()



def socialbundles2():
    sbundles2 = input(
        "1. WTF(Whatsapp, Twitter, Facebook) Bundles\n"
        "2. Youtube Bundles\n"
        "3. Opera Bundles\n"
        "4. Single Bundles\n"
        "5. Back\n"
    )
    if sbundles2 == "1":
        wtfBundles2()
    elif sbundles2 == "2":
        youtubeBundles2()
    elif sbundles2 == "3":
        operaBundles2()
    elif sbundles2 == "4":
        singleBundles2()
    elif sbundles2 == "5":
        giftDataPlan()
    else:
        print("Wrong input, Please try again")
        socialbundles2()


# nightandweekendplans under gift
def nightandweekendplans2():
    num = input(
        "Enter giftee number:\n"
    )
    if len(num) == 11 and num.isnumeric():
        print("Continue")
    else:
        print("Enter valid number")

    nAWP2 = input(
        "1. #25 = 250MB 1Day (12am-05am)\n"
        "2. #50 = 500MB 1Day (12am-05am)\n"
        "3. #100 = 1GB 5Days (12am-05am)\n"
        "4. #200 = 1.25GB 1Day SUN\n"
        "5. #500 = 3GB 2Days SAT-SUN\n"
        "6. Back\n"
    )
    if nAWP2 == "1":
        print("You have credited", num, "with #25 valid for 1 day")
    elif nAWP2 == "2":
        print("You have credited", num, "with #50 valid for 1 day")
    elif nAWP2 == "3":
        print("You have credited", num, "with #100 valid for 5 days")
    elif nAWP2 == "4":
        print("You have credited", num, "with #200 valid for 1 day")
    elif nAWP2 == "5":
        print("You have credited", num, "with #500 valid for 2 days")
    elif nAWP2 == "6":
        giftDataPlan()
    else:
        print("Wrong input, Please wait")
        nightandweekendplans2()


def giftDataPlan():
    gDP = input(
        "Please select a plan to Gift\n"
        "1. Mini Plans\n"
        "2. Monthly Plans\n"
        "3. Mega Plans\n"
        "4. Super Mega Plans\n"
        "5. Special Data Offer\n"
        "6. Social Bundles\n"
        "7. Night and Weekend Plans\n"
        "# Next\n"
    )
    if gDP == "1":
        miniplans2()
    elif gDP == "2":
        monthlyplans2()
    elif gDP == "3":
        megaplans2()
    elif gDP == "4":
        supermegaplans2()
    elif gDP == "5":
        specialDataoffer2()
    elif gDP == "6":
        socialbundles2()
    elif gDP == "7":
        nightandweekendplans2()
    elif gDP == "#":
        data()
    else:
        print("Wrong input, Please wait")
        giftDataPlan()


# miniplans for gift
def miniplans2():
    num = input(
        "Enter giftee number:\n"
    )
    if len(num) == 11 and num.isnumeric():
        print("Continue")
    else:
        print("Enter valid number")

    mp2 = input(
        "1. #100=150MB 1 Day icl 350MB nite\n"
        "2. #200=350MB 2 Days incl 110MB nite\n"
        "3. #500=1.8GB 14 Days incl 1GB nite\n"
        "4. #50=50MB 1 Day incl 5MB nite\n"
        "5. More plans\n"
        "6. Back\n"
    )
    if mp2 == "1":
        print("You have gifted", num, "with #100 naira valid for 1 day")
    elif mp2 == "2":
        print("You have gifted", num, "with #200 naira valid for 2 days")
    elif mp2 == "3":
        print("You have gifted", num, "with #500 naira valid for 14 days")
    elif mp2 == "4":
        print("You have gifted", num, "with #50 naira valid for 1 day")
    elif mp2 == "5":
        monthlyplans2()
    elif mp2 == "6":
        giftDataPlan()
    else:
        print("Wrong input, Please wait")
        miniplans2()


# monthlyplans for gift
def monthlyplans2():
    num = input(
        "Enter giftee number:\n"
    )
    if len(num) == 11 and num.isnumeric():
        print("Continue")
    else:
        print("Enter valid number")

    monPlans2 = input(
        "1. #1000=3.9GB 30Days incl 1GB nite\n"
        "2. #1500=7.5GB 30Days incl 4GB nite\n"
        "3. #2000=9.2GB 30Days incl 4GB nite\n"
        "4. #2500=10.8GB 30Days incl 4GB nite\n"
        "5. More Plans\n"
        "6. Back\n"
    )
    if monPlans2 == "1":
        print("You have gifted", num, "with #1000 valid for 30 days")
    elif monPlans2 == "2":
        print("You have gifted", num, "with #1500 valid for 30 days")
    elif monPlans2 == "3":
        print("You have gifted", num, "with #2000 valid for 30 days")
    elif monPlans2 == "4":
        print("You have gifted", num, "with #2500 valid for 30 days")
    elif monPlans2 == "5":
        moreMonthlyPlans()
    elif monPlans2 == "6":
        giftDataPlan()
    else:
        print("Wrong input, Please wait")
        monthlyplans2()


# moreplans under monthly
def moreMonthlyPlans():
    mMP = input(
        "1. #3000=14GB 30Days incl 4GB nite\n"
        "2. #4000=18GB 30Days incl 4GB nite\n"
        "3. #5000=24GB 30Days incl 4GB nite\n"
        "4. #8000=29.5GB 30Days incl 2BG nite\n"
        "5. More Plans\n"
        "6. Back\n"
    )
    if mMP == "1":
        print("You have been credited with #3000 valid for 30 days")
    elif mMP == "2":
        print("You have been credited with #4000 valid for 30 days")
    elif mMP == "3":
        print("You have been credited with #5000 valid for 30 days")
    elif mMP == "4":
        print("You have been credited with #8000 valid for 30 days")
    elif mMP == "5":
        megaplans()
    elif mMP == "6":
        monthlyplans()
    else:
        print("Wrong input, Please wait")
        moreMonthlyPlans()


# megaplans
# supermegaplans
def supermegaplans():
    sMP = input(
        "1. #30000=225GB 30 Days\n"
        "2. #36000=300GB 30Days\n"
        "3. #50000=425GB 90Days\n"
        "4. #60000=525GB 120Days\n"
        "5. #75000=675GB 120Days\n"
        "6. #100000=1024GB 1Year\n"
        "7. Back\n"
    )
    if sMP == "1":
        print("You have been credited with #30000 valid for 30 days")
    elif sMP == "2":
        print("You have been credited with #36000 valid for 30 days")
    elif sMP == "3":
        print("You have been credited with #50000 valid for 90 days")
    elif sMP == "4":
        print("You have been credited with #60000 valid for 120 days")
    elif sMP == "5":
        print("You have been credited with #75000 valid for 120 days")
    elif sMP == "6":
        print("You have been credited with #100000 valid for 1 year")
    elif sMP == '7':
        autorenew()
    else:
        print("Wrong input, Please wait")
        supermegaplans()


# autorenew
# specialdataoffer
# databooster
def dataBooster():
    dataB = input(
        "Data Booster adds volume to your current data plan\n"
        "1. #200 = 300MB (Daily or Weekly Plan Data\n"
        "2. #500 = 1GB (Monthly Plan Data Booster\n"
        "3. Back\n"
    )
    if dataB == "1":
        print("Your data plan has been boosted with 300MB")
    elif dataB == "2":
        print("Your data plan has been boosted with 1GB")
    elif dataB == "3":
        specialDataoffer()
    else:
        print("Wrong input, Please wait")
        dataBooster()


# minibadagryplans
def miniBadagryPlans():
    miniBP = input(
        "Get 10% extra data in Badagry\n"
        "1. #100 = 150MB 1Day incl 35MB nite\n"
        "2. #200 = 350MB 2 Days incl 110MB nite\n"
        "3. #500 = 1.35GB 14 Days incl 550MB nite\n"
        "4. #50 = 50MB 1 Day incl 5MB nite\n"
        "5. Back\n"
    )
    if miniBP == "1":
        print("You have been credited with #100 valid for 1 Day")
    elif miniBP == "2":
        print("You have been credited with #200 valid for 2 Days")
    elif miniBP == "3":
        print("You have been credited with #500 valid for 14 Days")
    elif miniBP == "4":
        print("You have been credited with #50 valid for 1 Day")
    elif miniBP == "5":
        badagryPlans()
    else:
        print("Wrong input, Please try again")
        miniBadagryPlans()


# monthlybadagryplans
def monthlyBadagryPlans():
    monthlyBP = input(
        "1. #1000=2.9GB 30Days incl 1GB nite\n"
        "2. #1500=4.1GB 30Days incl 600MB nite\n"
        "3. #2000=5.8GB 30Days incl 600MB nite\n"
        "4. #2500=7.7GB 30Days incl 900MB nite\n"
        "5. #3000=10GB 30Days incl 1GB nite\n"
        "6. #4000=13.25GB 30Days incl 1GB nite\n"
        "7. #5000=18.25GB 30Days incl 1.25GB nite\n"
        "8. #8000=29.5GB 30Days incl 2GB nite\n"
        "9. More Plans\n"
        "0. Back\n"
    )
    if monthlyBP == "1":
        print("You have been credited with #1000 valid for 30 days")
    elif monthlyBP == "2":
        print("You have been credited with #1500 valid for 30 days")
    elif monthlyBP == "3":
        print("You have been credited with #2000 valid for 30 days")
    elif monthlyBP == "4":
        print("You have been credited with #2500 valid for 30 days")
    elif monthlyBP == "5":
        print("You have been credited with #3000 valid for 30 days")
    elif monthlyBP == "6":
        print("You have been credited with #4000 valid for 30 days")
    elif monthlyBP == '7':
        print("You have been credited with #5000 valid for 30 days")
    elif monthlyBP == "8":
        print("You have been credited with #8000 valid for 30 days")
    elif monthlyBP == "9":
        megaBadagryPlans()
    elif monthlyBP == "0":
        badagryPlans()
    else:
        print("Wrong input, Please try again")
        monthlyBadagryPlans()


# megabadagryplans
def megaBadagryPlans():
    megaBP = input(
        "1. #10000=50GB 30Days incl 4GB nite\n"
        "2. #15000=93GB 30Days incl 7GB nite\n"
        "3. #18000=119GB 30Days incl 10GB nite\n"
        "4. #20000=138GB 30Days incl 12GB nite\n"
        "5. Back\n"
    )
    if megaBP == "1":
        print("You have been credited with #10000 valid for 30days")
    elif megaBP == "2":
        print("You have been credited with #15000 valid for 30 days")
    elif megaBP == "3":
        print("You have been credited with #18000 valid for 30 days")
    elif megaBP == "4":
        print("You have been credited with #20000 valid for 30 days")
    elif megaBP == "5":
        badagryPlans()
    else:
        print("Wrong input, Please try again")
        megaBadagryPlans()


# badagryplans
def badagryPlans():
    bP = input(
        "1. Mini Plans\n"
        "2. Monthly Plans\n"
        "3. Mega Plans\n"
        "4. Back\n"
        "5. Exit\n"
    )
    if bP == "1":
        miniBadagryPlans()
    elif bP == "2":
        monthlyBadagryPlans()
    elif bP == "3":
        megaBadagryPlans()
    elif bP == '4':
        specialDataoffer()
    elif bP == '5':
        print('Glo Unlimited')
    else:
        print('Wrong input, Please try again')
        badagryPlans()


# campusbooster
def campusBooster():
    cB = input(
        "1. #100 = 265MB 1 Day incl 35MB nite on campus\n"
        "2. #200 = 590MB 2 Days incl 110MB nite on campus\n"
        "3. #500 = 2.6GB 14 Days incl 1GB nite on campus\n"
        "4. #1000 = 5.8GB 30 Days incl 2GB nite on campus\n"
        "5. #2000 = 14.4GB 30 Days incl 4GB nite on campus\n"
        "6. #5000 = 44GB 30 Days incl 4GB nite on campus\n"
        "7. Back\n"
        "8. Exit\n"
    )
    if cB == "1":
        print("You have been credited with #100 valid for 1 day")
    elif cB == "2":
        print("You have been credited with #200 valid for 2 days")
    elif cB == "3":
        print("You have been credited with #500 valid for 14 days")
    elif cB == "4":
        print("You have been credited with #1000 valid for 30 days")
    elif cB == "5":
        print("You have been credited with #2000 valid for 30 days")
    elif cB == "6":
        print("You have been credited with #5000 valid for 30 days")
    elif cB == '7':
        specialDataoffer()
    elif cB == "8":
        print("Glo Unlimited")
    else:
        print("Wrong input, Please wait")
        campusBooster()


# specialplans
def specialplans():
    sP = input(
        "1. #300 = 1GB for 1 Day\n"
        "2. #500 = 2GB for 2 Days\n"
        "3. #1500 = 7GB for 7 Days\n"
        "4. Back\n"
        "0. Exit\n"
    )
    if sP == "1":
        print("You have been credited with #300 valid for 1 day")
    elif sP == "2":
        print("You have been credited with #500 valid for 2 days")
    elif sP == "3":
        print("You have been credited with #1500 valid for 7 days")
    elif sP == "4":
        specialDataoffer()
    elif sP == "0":
        print("Glo Unlimited")
    else:
        print("Wrong input, Please wait")
        specialplans()


def specialDataoffer():
    sDO = input(
        "1. Special Plans\n"
        "2. Campus Booster\n"
        "3. Badagry Plans\n"
        "4. Data Booster\n"
        "5. Back\n"
        "0. Exit\n"
    )
    if sDO == "1":
        specialplans()
    elif sDO == "2":
        campusBooster()
    elif sDO == "3":
        badagryPlans()
    elif sDO == "4":
        dataBooster()
    elif sDO == "5":
        autorenew()
    else:
        print('Glo Unlimited')


# socialbundles
# singlebundles
# instagrambundles
def instagramBundles():
    insta = input(
        "Instagram Bundles\n"
        "1. #25 = 20MB 1Day\n"
        "2. #50 = 50MB 7Days\n"
        "3. #100 = 125MB 30Days\n"
        "4. More Plans\n"
        "5. Back\n"
    )
    if insta == "1":
        print("You have been credited with #25 valid for 1 Day")
    elif insta == "2":
        print("You have been credited with #50 valid for 7 Days")
    elif insta == "3":
        print("You have been credited with #100 valid for 30 Days")
    elif insta == "4":
        print("Glo Unlimited")
    elif insta == "5":
        singleBundles()
    else:
        print("Wrong input, Please try again")
        instagramBundles()


# telegrambundles
def telegramBundles():
    telegram = input(
        "Telegram Bundles\n"
        "1. #25 = 20MB 1Day\n"
        "2. #50 = 50MB 7Days\n"
        "3. #100 = 125MB 30Days\n"
        "4. More Plans\n"
        "5. Back\n"
    )
    if telegram == "1":
        print("You have been credited with #25 valid for 1 Day")
    elif telegram == "2":
        print("You have been credited with #50 valid for 7 Days")
    elif telegram == "3":
        print("You have been credited with #100 valid for 30 Days")
    elif telegram == "4":
        instagramBundles()
    elif telegram == "5":
        singleBundles()
    else:
        print("Wrong input, Please try again")
        telegramBundles()


# tiktokbundles
def tiktokBundles():
    tiktok = input(
        "Tiktok Bundles\n"
        "1. #25 = 20MB 1Day\n"
        "2. #50 = 50MB 7Days\n"
        "3. #100 = 125MB 30Days\n"
        "4. More Plans\n"
        "5. Back\n"
    )
    if tiktok == "1":
        print("You have been credited with #25 valid for 1 Day")
    elif tiktok == "2":
        print("You have been credited with #50 valid for 7 Days")
    elif tiktok == "3":
        print("You have been credited with #100 valid for 30 Days")
    elif tiktok == "4":
        telegramBundles()
    elif tiktok == "5":
        singleBundles()
    else:
        print("Wrong input, Please try again")
        tiktokBundles()



def singleBundles():
    singlebundle = input(
        "1. Tiktok\n"
        "2. Telegram\n"
        "3. Instagram\n"
        "4. Back\n"
    )
    if singlebundle == "1":
        tiktokBundles()
    elif singlebundle == "2":
        telegramBundles()
    elif singlebundle == "3":
        instagramBundles()
    elif singlebundle == "4":
        socialbundles()
    else:
        print("Wrong input, Please try again")
        singleBundles()


# operabundles
def operaBundles():
    opBundles = input(
        "Opera Bundles\n"
        "1. #25 = 25MB 1Day\n"
        "2. #50 = 100MB 7Days\n"
        "3. #100 = 300MB 30Days\n"
        "4. More Plans\n"
        "5. Back\n"
    )
    if opBundles == "1":
        print("You have been credited with #25 valid for 1 Day")
    elif opBundles == "2":
        print("You have been credited with #50 valid for 7 Days")
    elif opBundles == "3":
        print("You have been credited with #100 valid for 30 Days")
    elif opBundles == "4":
        singleBundles()
    elif opBundles == "5":
        socialbundles()
    else:
        print("Wrong input, Please try again")
        operaBundles()


# youtubebundles
def youtubeBundles():
    ytBundles = input(
        "Youtube Bundles\n"
        "1. #50 = 100MB 1Day\n"
        "2. #50 = 1hour\n"
        "3. #50 = 5hours strasight\n"
        "4. #130 = 3hours\n"
        "5. #100 = 200MB 7Days\n"
        "6. #200 = 7hours night\n"
        "7. #250 = 500MB 30Days\n"
        "8. More Plans\n"
        "9. Back\n"
    )
    if ytBundles == "1":
        print("You have been credited with #50 valid for 1 Day")
    elif ytBundles == "2":
        print("You have been credited with #50 valid for 1 hour")
    elif ytBundles == "3":
        print("You have been credited with #50 valid for 5 hours")
    elif ytBundles == "4":
        print("You have been credited with #130 valid for 3 hours")
    elif ytBundles == "5":
        print("You have been credited with #100 valid for 7 Days")
    elif ytBundles == "6":
        print("You have been credited with #200 valid for 7 hours")
    elif ytBundles == "7":
        print("You have been credited with #250 valid for 30 Days")
    elif ytBundles == "8":
        operaBundles()
    elif ytBundles == "9":
        socialbundles()
    else:
        print("Wrong input, Please try again")
        youtubeBundles()


# WTFbundles
def wtfBundles():
    wtfbundles = input(
        "Whatsapp + Twitter + Facebook Bundles\n"
        "1. #25 = 100MB 1Day\n"
        "2. #50 = 200MB 7Days\n"
        "3. #100 = 500MB 30Days\n"
        "4. More Plans\n"
        "5. Back\n"
    )
    if wtfbundles == "1":
        print("You have been credited with #25 valid for 1 Day")
    elif wtfbundles == "2":
        print("You have been credited with #50 valid for 7 Days")
    elif wtfbundles == "3":
        print("You have been credited with #100 valid for 30 Days")
    elif wtfbundles == "4":
        youtubeBundles()
    elif wtfbundles == "5":
        socialbundles()
    else:
        print("Wrong input, Please try again")
        wtfBundles()


def socialbundles():
    sbundles = input(
        "1. WTF(Whatsapp, Twitter, Facebook) Bundles\n"
        "2. Youtube Bundles\n"
        "3. Opera Bundles\n"
        "4. Single Bundles\n"
        "5. Back\n"
    )
    if sbundles == "1":
        wtfBundles()
    elif sbundles == "2":
        youtubeBundles()
    elif sbundles == "3":
        operaBundles()
    elif sbundles == "4":
        singleBundles()
    elif sbundles == "5":
        autorenew()
    else:
        print("Wrong input, Please try again")
        socialbundles()


# nightandweekendplans
def nightandweekendplans():
    nAWP = input(
        "1. #25 = 250MB 1Day (12am-05am)\n"
        "2. #50 = 500MB 1Day (12am-05am)\n"
        "3. #100 = 1GB 5Days (12am-05am)\n"
        "4. #200 = 1.25GB 1Day SUN\n"
        "5. #500 = 3GB 2Days SAT-SUN\n"
        "6. Back\n"
    )
    if nAWP == "1":
        print("You have been credited with #25 valid for 1 day")
    elif nAWP == "2":
        print("You have been credited with #50 valid for 1 day")
    elif nAWP == "3":
        print("You have been credited with #100 valid for 5 days")
    elif nAWP == "4":
        print("You have been credited with #200 valid for 1 day")
    elif nAWP == "5":
        print("You have been credited with #500 valid for 2 days")
    elif nAWP == "6":
        autorenew()
    else:
        print("Wrong input, Please wait")
        nightandweekendplans()


# buydataplan
# oneoff
# showmax data plans
def showmaxplans():
    showMaxData = input(
        "Please Select\n"
        "1. Showmax Mobile Only Access -#1200, 30 Days\n"
        "2. Showmax Mobile -#1400, 1.5GB, 30 Days\n"
        "3. Showmax Mobile  -#1700, 3GB, 30 Days\n"
        "4. Showmax Pro Only Access -#3200, 30 Days\n"
        "5. Showmax Pro -#3400, 3GB, 30 Days\n"
        "6. Showmax Pro -#3700, 5GB, 30 Days\n"
        "7. Back\n"
        "0. Exit\n"
    )
    if showMaxData == "1":
        print("You have successfully subscribed to Showmax Mobile Only Access")
    elif showMaxData == "2":
        print("You have successfully subscribed to Showmax Mobile")
    elif showMaxData == "3":
        print("You have successfully subscribed to Showmax Mobile")
    elif showMaxData == "4":
        print("You have successfully subscribed to Showmax Pro Only Access")
    elif showMaxData == "5":
        print("You have successfully subscribed to Showmax Pro")
    elif showMaxData == "6":
        print("You have successfully subscribed to Showmax Pro")
    elif showMaxData == "7":
        oneoff()
    elif showMaxData == "0":
        print('Glo Unlimited')
    else:
        print("Wrong input, Please wait")
        showmaxplans()


def oneoff():
    oo = input(
        "1. Mini Plans\n"
        "2. Monthly Plans\n"
        "3. Mega Plans\n"
        "4. Super Mega Plans\n"
        "5. Showmax Data Plans\n"
        "6. Special Data Offer\n"
        "7. Social Bundles\n"
        "8. Night and Weekend Plans\n"
        "99. Back\n"
        "0. Exit\n"
    )
    if oo == "1":
        miniplans()
    elif oo == "2":
        monthlyplans()
    elif oo == "3":
        megaplans()
    elif oo == "4":
        supermegaplans()
    elif oo == "5":
        showmaxplans()
    elif oo == "6":
        specialDataoffer()
    elif oo == "7":
        socialbundles()
    elif oo == "8":
        nightandweekendplans()
    elif oo == "99":
        buydataplan()
    elif oo == "0":
        print("Glo Unlimited")
    else:
        print("Wrong input, Please wait")
        oneoff()


def buydataplan():
    dp = input(
        "1. Proceed(Auto-Renew)\n"
        "2. Proceed(One-off)\n"
        "0. Back\n")
    if dp == "1":
        autorenew()
    elif dp == "2":
        oneoff()
    else:
        buydataplan()


def autorenew():
    ar = input(
        "1. Mini Plans\n"
        "2. Monthly Plans\n"
        "3. Mega Plans\n"
        "4. Super Mega Plans\n"
        "5. Special Data Offer\n"
        "6. Social Bundles\n"
        "7. Night and Weekend Plans\n"
        "8. Back\n"
        "0. Exit\n"
    )
    if ar == "1":
        miniplans()
    elif ar == "2":
        monthlyplans()
    elif ar == "3":
        megaplans()
    elif ar == "4":
        supermegaplans()
    elif ar == "5":
        specialDataoffer()
    elif ar == "6":
        socialbundles()
    elif ar == "7":
        nightandweekendplans()
    elif ar == "8":
        buydataplan()
    elif ar == "0":
        print("Glo Unlimited")
    else:
        print("Wrong input, Please wait")
        autorenew()


# miniplans
def miniplans():
    mp = input(
        "1. #100=150MB 1 Day icl 350MB nite\n"
        "2. #200=350MB 2 Days incl 110MB nite\n"
        "3. #500=1.8GB 14 Days incl 1GB nite\n"
        "4. #50=50MB 1 Day incl 5MB nite\n"
        "5. More plans\n"
        "6. Back\n"
    )
    if mp == "1":
        print("You have been credited with #100 valid for 1 day")
    elif mp == "2":
        print("You have been credited with #200 valid for 2 days")
    elif mp == "3":
        print("You have been credited with #500 valid for 14 days")
    elif mp == "4":
        print("You have been credited with #50 valid for 1 day")
    elif mp == "5":
        monthlyplans()
    elif mp == "6":
        autorenew()
    else:
        print("Wrong input, Please wait")
        miniplans()


def megaplans():
    megaP = input(
        "1. #10000=50GB 30Days incl 4GB nite\n"
        "2. #15000=93GB 30Days incl 7GB nite\n"
        "3. #18000=119GB 30Days incl 10GB nite\n"
        "4. #20000=138GB 30Days incl 12BG nite\n"
        "5. More Plans\n"
        "6. Back\n"
    )
    if megaP == "1":
        print("You have been credited with #10000 valid for 30 days")
    elif megaP == "2":
        print("You have been credited with #15000 valid for 30 days")
    elif megaP == "3":
        print("You have been credited with #18000 valid for 30 days")
    elif megaP == "4":
        print("You have been credited with #20000 valid for 30 days")
    elif megaP == "5":
        supermegaplans()
    elif megaP == "6":
        autorenew()
    else:
        print("Wrong input, Please wait")
        megaplans()


# monthlyplans
def monthlyplans():
    monPlans = input(
        "1. #1000=3.9GB 30Days incl 1GB nite\n"
        "2. #1500=7.5GB 30Days incl 4GB nite\n"
        "3. #2000=9.2GB 30Days incl 4GB nite\n"
        "4. #2500=10.8GB 30Days incl 4GB nite\n"
        "5. More Plans\n"
        "6. Back\n"
    )
    if monPlans == "1":
        print("You have been credited with #1000 valid for 30 days")
    elif monPlans == "2":
        print("You have been credited with #1500 valid for 30 days")
    elif monPlans == "3":
        print("You have been credited with #2000 valid for 30 days")
    elif monPlans == "4":
        print("You have been credited with #2500 valid for 30 days")
    elif monPlans == "5":
        moreMonthlyPlans()
    elif monPlans == "6":
        autorenew()
    else:
        print("Wrong input, Please wait")
        monthlyplans()


# supermegaplans under gift data
def supermegaplans2():
    num = input(
        "Enter giftee number:\n"
    )
    if len(num) == 11 and num.isnumeric():
        print("Continue")
    else:
        print("Enter valid number")

    sMP2 = input(
        "1. #30000=225GB 30 Days\n"
        "2. #36000=300GB 30Days\n"
        "3. #50000=425GB 90Days\n"
        "4. #60000=525GB 120Days\n"
        "5. #75000=675GB 120Days\n"
        "6. #100000=1024GB 1Year\n"
        "7. Back\n"
    )
    if sMP2 == "1":
        print("You have gifted", num, "with #30000 valid for 30 days")
    elif sMP2 == "2":
        print("You have gifted", num, "with #36000 valid for 30 days")
    elif sMP2 == "3":
        print("You have gifted", num, "with #50000 valid for 90 days")
    elif sMP2 == "4":
        print("You have gifted", num, "with #60000 valid for 120 days")
    elif sMP2 == "5":
        print("You have gifted", num, "with #75000 valid for 120 days")
    elif sMP2 == "6":
        print("You have gifted", num, "with #100000 valid for 1 year")
    elif sMP2 == '7':
        giftDataPlan()
    else:
        print("Wrong input, Please wait")
        supermegaplans2()


# megaplans under gift plans
def megaplans2():
    num = input(
        "Enter giftee number:\n"
    )
    if len(num) == 11 and num.isnumeric():
        print("Continue")
    else:
        print("Enter valid number")

    megaP2 = input(
        "1. #10000=50GB 30Days incl 4GB nite\n"
        "2. #15000=93GB 30Days incl 7GB nite\n"
        "3. #18000=119GB 30Days incl 10GB nite\n"
        "4. #20000=138GB 30Days incl 12BG nite\n"
        "5. More Plans\n"
        "6. Back\n"
    )
    if megaP2 == "1":
        print("You have gifted", num, "with #10000 valid for 30 days")
    elif megaP2 == "2":
        print("You have gifted", num, "with #15000 valid for 30 days")
    elif megaP2 == "3":
        print("You have gifted", num, "with #18000 valid for 30 days")
    elif megaP2 == "4":
        print("You have gifted", num, "with #20000 valid for 30 days")
    elif megaP2 == "5":
        supermegaplans2()
    elif megaP2 == "6":
        giftDataPlan()
    else:
        print("Wrong input, Please wait")
        megaplans2()


# matchdayspecialoffer
def matchdayOffer():
    print("Sorry, there are no Special Offers at the moment.\n"
          "Next offer will be available in 7m:17s\n")
    data()


def data():
    dataTrans = input(
        "1. Buy Data Plan\n"
        "2. Match Day Special Offer\n"
        "3. Gift Data Plan\n"
        "4. Share Data Plan\n"
        "5. Check Data Balance\n"
        "6. Manage Data Balance\n"
        "7. Blackberry\n"
        "8. Back\n"
        "9. Exit\n"
    )
    if dataTrans == "1":
        # Buy Data Plans
        dataPlan()
    elif dataTrans == "2":
        # Match day spec
        matchdayOffer()
    elif dataTrans == "3":
        # Gift data
        giftDataPlan()
    elif dataTrans == "4":
        # Share data
        shareDataPlan()
    elif dataTrans == "5":
        # Data balance
        print("You are on a #1000, expires 09/12/2022 13:05,\n"
              "Your data balance 1492MB, browsed for 275 Min\n"
              "renewal status ACCEPTED\n")
    elif dataTrans == "6":
        #Manage data bal
        manageDataPlan()
    elif dataTrans == "7":
        # Blackberry
        blackberry()
    elif dataTrans == "8":
        # Back
        selectTrans()
    elif dataTrans == "9":
        # Exit
        ussd()

    else:
        print(
            "Invalid Entry\n"
            "Try Again"
        )
        data()


def feastJoy():
    print(
        "Get a chance to win 20 HOUSES, 24 CARS, 100 GENERATORS\n"
        "200, SEWING MACHINES, 1000 RECHARGEABLE FANS & more\n"
        "in the Glo Festival of Joy Promo\n"
    )
    feast = input(
        "1. To Participate\n"
        "2. Back\n"
    )
    if feast == "1":
        print("Thanks! We look forward to your participation at\n"
              "year end consumer promo, recharge minimum of #500\n"
              "today and stand a chance to win any of daily, weekly\n"
              "or monthly prizes")
    elif feast == "2":
        # Back
        selectTrans()
    else:
        print(
            "Invalid Transaction Entry\n"
            "Try Again"
        )
        feastJoy()


# E-topup
def eTop():
    print("E-Topup\n")
    topUp = input(
        "Welcome to Glo e-Services\n"
        "Please select an option:\n"
        "1. Airtime\n"
        "2. Data\n"
        "0. Exit\n"
    )
    if topUp == "1":
        eAirtime()
    elif topUp == "2":
        eData()
    elif topUp == "0":
        print("Glo Unlimited")
    else:
        print("Wrong input, try again")
        eTop()


# Data under E-top up
def eData():
    purchase()


# Airtime under E-top up
def eAirtime():
    print("E-Airtime\n")
    eAT = input(
        "Please select type of Airtime\n"
        "1. 5X Recharges\n"
        "2. Regular Recharges\n"
        "0. Back\n"
    )
    if eAT == "1":
        fiveRecharge()
    elif eAT == '2':
        print('Airtime Purchase')
        purchase()
    elif eAT == "0":
        eTop()
    else:
        print("Wrong input")
        eAirtime()


# purchase of airtime/data
def purchase():
    owner = input(
        "1. Self\n"
        "2. Third party\n"
        "00. Back\n"
    )
    if owner == "1":
        r = input("Please enter amount: \n")
        print("You have been credited with ", r, "naira")
    elif owner == "2":
        num = input("Please enter phone number: \n"
                    "Glo line only\n")
        r1 = input("Please enter amount: ")
        if num.isnumeric() and len(num) == 11:
            print(f"{num} has been credited with ", r1, "naira")
    elif owner == "00":
        eAirtime()
    else:
        print("Wrong input")
        purchase()


# 5X recharges
def fiveRecharge():
    print("5X Recharge\n")
    frecharge = input(
        "1. #120\n"
        "2. #220\n"
        "3. #320\n"
        "4. #420\n"
        "5. #520\n"
        "6. #620\n"
        "7. #720\n"
        "8. More\n"
        "9. Back\n"
    )
    if frecharge == "1":
        print("Your account has been credited with 100 naira")
    elif frecharge == "2":
        print("Your account has been credited with 200 naira")
    elif frecharge == "3":
        print("Your account has been credited with 300 naira")
    elif frecharge == "4":
        print("Your account has been credited with 400 naira")
    elif frecharge == "5":
        print("Your account has been credited with 500 naira")
    elif frecharge == "6":
        print("Your account has been credited with 600 naira")
    elif frecharge == "7":
        print("Your account has been credited with 700 naira")
    elif frecharge == "8":
        moreFiverecharge()
    elif frecharge == "9":
        eAirtime()
    else:
        print("Wrong input, please try again")
        fiveRecharge()


# morefiverecharge
def moreFiverecharge():
    moreFrecharge = input(
        "1. #820\n"
        "2. #920\n"
        "3. #1020\n"
        "4. #1220\n"
        "5. Back\n"
    )
    if moreFrecharge == "1":
        print("Your account has been credited with 800 naira")
    elif moreFrecharge == "2":
        print("Your account has been credited with 900 naira")
    elif moreFrecharge == "3":
        print("Your account has been credited with 1000 naira")
    elif moreFrecharge == "4":
        print("Your account has been credited with 1200 naira")
    elif moreFrecharge == "5":
        fiveRecharge()
    else:
        print('Wrong input, Please try again')
        moreFiverecharge()


# Berekete10x
def berekete():
    bk = input(
        "Enjoy 700% bonus to call all networks + FREE Data on every recharge\n"
        "1. Migrate Now\n"
        "2. Back\n"
        "3. Exit\n"
    )
    if bk == "1":
        print("Dear customer, you are now on Glo Berekete 10X\n"
              "Recharge #100 and make a call to get #1000 sign-on\n"
              "bonus. Also enjoy 10X bonus on all recharges for calls and data\n"
              )
    elif bk == "2":
        selectTrans()
    elif bk == "3":
        print("Glo Unlimited")
    else:
        print("Wrong input, please try again")
        berekete()


# Tariff Plan

# checkbalancefortariff
def checkBalance():
    cBalance = input(
        '1. Main Balance\n'
        '2. Promo Account 1\n'
        '3. Promo Account 2\n'
        '4. Back\n'
        '5. Exit\n'
    )
    if cBalance == "1":
        print("Your account balance is #0.68. Please recharge as soon as possible")
    elif cBalance == "2":
        print("Your promo account balance is #0.00")
    elif cBalance == "3":
        print("Your promo account balance is #0.00")
    elif cBalance == "4":
        tariffPlan()
    elif cBalance == "5":
        print("Glo Unlimited")
    else:
        print('Wrong Code')
        checkBalance()


# otherPlans under tarrifs
def alwaysOn():
    gloAO = input(
        'You are opting to migrate to Glo Always On.\n'
        'You will be charged #500 for this annual subscription plan.\n'
        'Press\n'
        '1. To migrate\n'
        '2. Back\n'
        '0. Exit\n'
    )
    if gloAO == "1":
        print("You have successfully migrated to Glo Always On!")
    elif gloAO == "2":
        otherPlans()
    elif gloAO == "0":
        print("Glo Unlimited")
    else:
        print('Wrong Code')
        alwaysOn()


def TwentytwoPlan():
    plan22 = input(
        "Get 22 times value on every recharge to call all\n"
        "networks, text, chat and browse:\n"
        "1. Migrate Now\n"
        "2. Back\n"
        "3. Exit\n"
    )
    if plan22 == "1":
        print("You have successfully migrated to 22X Plan!")
    elif plan22 == "2":
        otherPlans()
    elif plan22 == "3":
        print("Glo Unlimited")
    else:
        print('Wrong Code')
        TwentytwoPlan()


def gbamPlus():
    gbam = input(
        "Special rate of 11k/sec onnet and 18k/sec for offnet,\n"
        "#4/SMS Daily Rental of #5.\n"
        "To Subscribe, press:\n"
        "1. *211#\n"
        "2. Back\n"
        "3. Exit\n"
    )
    if gbam == "1" or gbam == '*211#':
        print("You have successfully subscribed to Glo's Gbam Plus!")
    elif gbam == "2":
        otherPlans()
    elif gbam == "3":
        print("Glo Unlimited")
    else:
        print('Wrong Code')
        gbamPlus()


def otherPlans():
    oPlans = input(
        "1. Always On- 365days Validity\n"
        "2. 22X Plan\n"
        "3. Gbam Plus\n"
        "4. Back\n"
        "5. Exit\n"
    )
    if oPlans == "1":
        alwaysOn()
    elif oPlans == "2":
        TwentytwoPlan()
    elif oPlans == "3":
        gbamPlus()
    elif oPlans == "4":
        tariffPlan()
    elif oPlans == "5":
        print("Glo Unlimited")
    else:
        print('Wrong Code')
        otherPlans()


# voice offers for tarrif

# naira multiplier under voiceoffers
def nairaMultiplier():
    nM = input(
        "Naira Multiplier\n"
        "1. Pay #100 Get #300 3 Day\n"
        "2. Pay #300 Get #1000 7 Days\n"
        "3. Pay #500 Get #1800 10 Days\n"
        "4. Pay #1000 Get #4000 15 Days\n"
        "5. Pay #15000 Get #6000 30 Days\n"
        "6. Back\n"
        "0. Exit\n"
    )
    if nM == "1":
        print("Your account has been successfully credited with #300 for 3 Days")
    elif nM == "2":
        print("Your account has been successfully credited with #1000 for 7 Days")
    elif nM == "3":
        print("Your account has been successfully credited with #1800 for 10 Days")
    elif nM == "4":
        print("Your account has been successfully credited with #4000 for 15 Days")
    elif nM == "5":
        print("Your account has been successfully credited with #6000 for 30 Days")
    elif nM == "6":
        voiceOffers()
    elif nM == "0":
        print("Glo Unlimited")
    else:
        print("Wrong input")
        nairaMultiplier()


# call 18 countries under voice offers
# IDD Call Slasher under call countries
def iddslasher1():
    idds1 = input(
        "Enjoy the lowest IDD tariffs(up to 25% discounts) to\n"
        "call over 200 destinations at #200/month. Valid for 30 Days\n"
        "1. Subscribe(#200/month)\n"
        "2. Unsubscribe\n"
        "3. Back\n"
        "0. Exit\n"
    )
    if idds1 == "1":
        print("You have successfully subscribed to Glo's IDD Call Slasher at #200/month!")
    elif idds1 == "2":
        print("You have successfully unsubscribed from Glo's IDD Call Slasher!")
    elif idds1 == "3":
        callCountries()
    elif idds1 == "0":
        print("Glo Unlimited")
    else:
        print("Wrong code")
        iddslasher1()


def callCountries():
    cc = input(
        "1. IDD Call Slasher\n"
        "2. #100 = 9 Mins 3 Days\n"
        "3. #200 = 19 Mins 7 Days\n"
        "4. #500 = 43 Mins 14 Days\n"
        "5. #1000 = 93 Mins 30 Days\n"
        "6. List of 16 Countries\n"
        "7. IDD Pack Bal\n"
        "8. Back\n"
        "0. Exit\n"
    )
    if cc == "1":
        iddslasher1()
    elif cc == "2":
        print("Your account has been successfully credited with #100 for 3 Days")
    elif cc == "3":
        print("Your account has been successfully credited with #200 for 7 Days")
    elif cc == "4":
        print("Your account has been successfully credited with #500 for 14 Days")
    elif cc == "5":
        print("Your account has been successfully credited with #1000 for 30 Days")
    elif cc == "6":
        print("Canada, China, India, Ireland, Malaysia, Uk\n"
              "USA, Singapore, Porto Rico, S.Korea, Israel, Romania\n")
        fg = input(
            "1. Back\n"
            "2. Exit\n"
        )
        if fg == "1":
            voiceOffers()
        elif fg == "2":
            print("Glo Unlimited")
        else:
            pass
    elif cc == "7":
        print("1DD-16 countries pack balance in seconds:\n"
              "IDD-100:0; IDD-200:0; IDD-500:0; IDD-1000:0\n")
    elif cc == "8":
        voiceOffers()
    elif cc == "0":
        print("Glo Unlimited")
    else:
        print("Wrong input")
        callCountries()


# super hot deals under voice offers
def superHotDeals():
    sHD = input(
        "SUPER HOT MONTHLY DEALS\n"
        "1. Free Tomorrow\n"
        "2. Big 200% Bonus\n"
        "3. All Calls @ 12k/sec\n"
        "4. Back\n"
        "0. Exit\n"
    )
    if sHD == "1":
        print("You have successfully activated Free Tomorrow, valid for 30 Days")
    elif sHD == "2":
        print("You have successfully activated the Big 200% Bonus, valid for 30 Days")
    elif sHD == "3":
        print("You have successfully activated all calls @ 12k/sec valid for 30 Days")
    elif sHD == "4":
        voiceOffers()
    elif sHD == "0":
        print("Glo Unlimited")
    else:
        print("Wrong Code")
        superHotDeals()


# checkbalance under voiceoffers
def checkBalance2():
    cBalance2 = input(
        '1. Main Balance\n'
        '2. Promo Account 1\n'
        '3. Back\n'
        '0. Exit\n'
    )
    if cBalance2 == "1":
        print("Your account balance is #0.68. Please recharge as soon as possible")
    elif cBalance2 == "2":
        print("Your promo account balance is #0.00")
    elif cBalance2 == "3":
        voiceOffers()
    elif cBalance2 == "0":
        print("Glo Unlimited")
    else:
        print('Wrong Code')
        checkBalance2()


# glo amebo under voiceoffers
def gloAmebo():
    gAmebo = input(
        "Now enjoy 5 times of your recharge value to call,\n"
        "browse and SMS.\n"
        "Please enter your Glo Recharge Pin Now: \n"
    )
    if gAmebo == "*123*":
        print("You have successfully subscribed to Glo Amebo!")
    else:
        print("Wrong code")
        gloAmebo()


# super value pack under voiceoffers
def superValuePack():
    sVP = input(
        "1. Glo Super Value Recharge\n"
        "2. Super Value Balance\n"
        "3. Back\n"
        "0. Exit\n"
    )
    if sVP == "1":
        print("There are currently no available options\n"
              "Please try again later.\n")
    elif sVP == "2":
        print("You are not subscribed to super Value Pack.\n"
              "Your balance is #0.00\n")
    elif sVP == "3":
        voiceOffers()
    elif sVP == "0":
        print("Glo Unlimited")


def voiceOffers():
    vO = input(
        "HOT DEALS\n"
        "1. Naira Multiplier\n"
        "2. Call 18 Countries @ Local Rates\n"
        "3. Super Hot Monthly Deals\n"
        "4. Check your balance\n"
        "5. GLO Amebo-5X\n"
        "6. Super Value Pack\n"
        "7. Back\n"
        "0. Exit\n"
    )
    if vO == "1":
        nairaMultiplier()
    elif vO == "2":
        callCountries()
    elif vO == "3":
        superHotDeals()
    elif vO == "4":
        checkBalance2()
    elif vO == "5":
        gloAmebo()
    elif vO == "6":
        superValuePack()
    elif vO == "7":
        tariffPlan()
    elif vO == "0":
        print("Glo Unlimited")
    else:
        print('Wrong Code')
        voiceOffers()


def tariffPlan():
    tarPlan = input(
        "1. My Package\n"
        "2. Check Balance\n"
        "3. My Number\n"
        "4. Friends & Family Numbers\n"
        "5. Recharge\n"
        "6. Other Plans\n"
        "7. Voice Offers\n"
        "8. Back\n"
        "0. Exit\n"
    )
    if tarPlan == "1":
        print("Dear Customer, your profile is GLO_BEREKETE")
    elif tarPlan == "2":
        checkBalance()
    elif tarPlan == "3":
        print("An error has occurred, Please try again later")
    elif tarPlan == "4":
        print("An error has occurred, Please try again later")
    elif tarPlan == "5":
        print("Glo Unlimited")
    elif tarPlan == "6":
        otherPlans()
    elif tarPlan == "7":
        voiceOffers()
    elif tarPlan == "8":
        selectTrans()
    elif tarPlan == "0":
        print("Glo Unlimited")
    else:
        print("Wrong code")
        tariffPlan()


# international calls and roaming
def intCallsAndRoaming():
    iCR = input(
        "1. Int'l Call Offers\n"
        "2. Data Roaming Bundles\n"
        "3. Back\n"
        "0. Exit\n"
    )
    if iCR == "1":
        intCallOffers()
    elif iCR == "2":
        dataRoamingBundles()
    elif iCR == "3":
        selectTrans()
    elif iCR == "0":
        print("Glo Unlimited")
    else:
        print("Wrong code")
        intCallsAndRoaming()


# intl call offers under icr
# IDD Call Slasher
def iddslasher():
    idds = input(
        "Enjoy the lowest IDD tariffs(up to 25% discounts) to\n"
        "call over 200 destinations at #200/month. Valid for 30 Days\n"
        "1. Subscribe(#200/month)\n"
        "2. Unsubscribe\n"
        "3. Back\n"
        "0. Exit\n"
    )
    if idds == "1":
        print("You have successfully subscribed to Glo's IDD Call Slasher at #200/month!")
    elif idds == "2":
        print("You have successfully unsubscribed from Glo's IDD Call Slasher!")
    elif idds == "3":
        intCallOffers()
    elif idds == "0":
        print("Glo Unlimited")
    else:
        print("Wrong code")
        iddslasher()


# IDD CALL PACKS
def iddCallPacks():
    iddCP = input(
        "1. Proceed (Auto-Renew)\n"
        "2. Proceed (One Time)\n"
        "0. Exit\n"
    )
    if iddCP == "1":
        iddAutorenew()
    elif iddCP == "2":
        iddOneTime()
    elif iddCP == "0":
        print("Glo Unlimited")
    else:
        print("Wrong code")
        iddCallPacks()


# iddAUTORENEW
def iddAutorenew():
    idddAR = input(
        "1. #100 = 9 Min 3 Days\n"
        "2. #200 = 19 Min 7 Days\n"
        "3. #500 = 43 Min 14 Days\n"
        "4. #1000 = 93 Min 30 Days\n"
        "5. List of 16 countries\n"
        "6. IDD Pack Bal\n"
        "7. Back\n"
        "8. Exit\n"
    )
    if idddAR == "1":
        print("You have successfully subscribed to Glo's IDD Call Pack at #100 for 3 Days!")
    elif idddAR == "2":
        print("You have successfully subscribed to Glo's IDD Call Pack at #200 for 7 Days!")
    elif idddAR == "3":
        print("You have successfully subscribed to Glo's IDD Call Pack at #500 for 14 Days!")
    elif idddAR == "4":
        print("You have successfully subscribed to Glo's IDD Call Pack at #1000 for 30 Days!")
    elif idddAR == "5":
        print("Canada, China, India, Ireland, Malaysia, Uk\n"
              "USA, Singapore, Porto Rico, S.Korea, Israel, Romania\n")
        fg = input(
            "1. Back\n"
            "2. Exit\n"
        )
        if fg == "1":
            iddAutorenew()
        elif fg == "2":
            print("Glo Unlimited")
        else:
            pass
    elif idddAR == "6":
        print("1DD-16 countries pack balance in seconds:\n"
              "IDD-100:0; IDD-200:0; IDD-500:0; IDD-1000:0\n")
    elif idddAR == "7":
        iddCallPacks()
    elif idddAR == "8":
        print("Glo Unlimited")
    else:
        print("Wrong code")
        iddAutorenew()


# iddOnetime
def iddOneTime():
    iddOT = input(
        "1. #100 = 9 Min 3 Days\n"
        "2. #200 = 19 Min 7 Days\n"
        "3. #500 = 43 Min 14 Days\n"
        "4. #1000 = 93 Min 30 Days\n"
        "5. List of 16 countries\n"
        "6. IDD Pack Bal\n"
        "7. Back\n"
        "8. Exit\n"
    )
    if iddOT == "1":
        print("You have successfully subscribed to Glo's IDD Call Pack at #100 for 3 Days!")
    elif iddOT == "2":
        print("You have successfully subscribed to Glo's IDD Call Pack at #200 for 7 Days!")
    elif iddOT == "3":
        print("You have successfully subscribed to Glo's IDD Call Pack at #500 for 14 Days!")
    elif iddOT == "4":
        print("You have successfully subscribed to Glo's IDD Call Pack at #1000 for 30 Days!")
    elif iddOT == "5":
        print("Canada, China, India, Ireland, Malaysia, Uk\n"
              "USA, Singapore, Porto Rico, S.Korea, Israel, Romania\n")
        fg = input(
            "1. Back\n"
            "2. Exit\n"
        )
        if fg == "1":
            iddOneTime()
        elif fg == "2":
            print("Glo Unlimited")
        else:
            pass
    elif iddOT == "6":
        print("1DD-16 countries pack balance in seconds:\n"
              "IDD-100:0; IDD-200:0; IDD-500:0; IDD-1000:0\n")
    elif iddOT == "7":
        iddCallPacks()
    elif iddOT == "8":
        print("Glo Unlimited")
    else:
        print("Wrong code")
        iddOneTime()


def intCallOffers():
    iCO = input(
        "1. IDD Call Slasher\n"
        "2. IDD Call Packs\n"
        "3. Back\n"
        "0. Exit\n"
    )
    if iCO == "1":
        iddslasher()
    elif iCO == "2":
        iddCallPacks()
    elif iCO == "3":
        intCallsAndRoaming()
    elif iCO == "0":
        print("Glo Unlimited")
    else:
        print("Wrong code")
        intCallOffers()


# data roaming bundles under icr
def dataRoamingBundles():
    dRB = input(
        '1. Zone1: USA, CAN, GHA, FRAN\n'
        '2. Zone2: IND, CHINA, NETHD, GERM, SAUDI\n'
        '3. Zone3: BENIN\n'
        '4. Zone4: NIGER, SWITZER, UAE\n'
        '5. Back\n'
        '0. Exit\n'
    )
    if dRB == "1":
        zoneOne()
    elif dRB == "2":
        zoneTwo()
    elif dRB == "3":
        zoneThree()
    elif dRB == "4":
        zoneFour()
    elif dRB == "5":
        intCallsAndRoaming()
    elif dRB == "0":
        print("Glo Unlimited")
    else:
        print("Wrong Code")
        dataRoamingBundles()


# zone1
def zoneOne():
    zone1 = input(
        'ZONE 1: USA, CAN, GHA, FRAN\n'
        '1. #500 = 3 Days pack 200MB\n'
        '2. #1000 = 7 Days pack 500MB\n'
        '3. #2000 = 15 Days pack 1GB\n'
        '4. Back\n'
        '0. Exit\n'
    )
    if zone1 == "1":
        print("You have been credited successfully with #500 for 3 Days!")
    elif zone1 == "2":
        print("You have been credited successfully with #1000 for 7 Days!")
    elif zone1 == "3":
        print("You have been credited successfully with #2000 for 15 Days!")
    elif zone1 == "4":
        dataRoamingBundles()
    elif zone1 == "0":
        print("Glo Unlimited")
    else:
        print("Wrong code")
        zoneOne()


# zone2
def zoneTwo():
    zone2 = input(
        'ZONE 2: IND, CHINA, NETHD, GERM, SAUDI\n'
        '1. #1000 = 3 Days pack 200MB\n'
        '2. #2000 = 7 Days pack 500MB\n'
        '3. #4000 = 15 Days pack 1GB\n'
        '4. Back\n'
        '0. Exit\n'
    )
    if zone2 == "1":
        print("You have been credited successfully with #1000 for 3 Days!")
    elif zone2 == "2":
        print("You have been credited successfully with #2000 for 7 Days!")
    elif zone2 == "3":
        print("You have been credited successfully with #4000 for 15 Days!")
    elif zone2 == "4":
        dataRoamingBundles()
    elif zone2 == "0":
        print("Glo Unlimited")
    else:
        print("Wrong code")
        zoneTwo()


# zone3
def zoneThree():
    zone3 = input(
        'ZONE 3: BENIN\n'
        '1. #2000 = 3 Days pack 200MB\n'
        '2. #5000 = 7 Days pack 500MB\n'
        '3. #10000 = 15 Days pack 1GB\n'
        '4. Back\n'
        '0. Exit\n'
    )
    if zone3 == "1":
        print("You have been credited successfully with #2000 for 3 Days!")
    elif zone3 == "2":
        print("You have been credited successfully with #5000 for 7 Days!")
    elif zone3 == "3":
        print("You have been credited successfully with #10000 for 15 Days!")
    elif zone3 == "4":
        dataRoamingBundles()
    elif zone3 == "0":
        print("Glo Unlimited")
    else:
        print("Wrong code")
        zoneThree()


# zone4
def zoneFour():
    zone4 = input(
        'ZONE 4: NIGER, SWITZER, UAE\n'
        '1. #3000 = 3 Days pack 200MB\n'
        '2. #8000 = 7 Days pack 500MB\n'
        '3. #15000 = 15 Days pack 1GB\n'
        '4. Back\n'
        '0. Exit\n'
    )
    if zone4 == "1":
        print("You have been credited successfully with #3000 for 3 Days!")
    elif zone4 == "2":
        print("You have been credited successfully with #8000 for 7 Days!")
    elif zone4 == "3":
        print("You have been credited successfully with #15000 for 15 Days!")
    elif zone4 == "4":
        dataRoamingBundles()
    elif zone4 == "0":
        print("Glo Unlimited")
    else:
        print("Wrong code")
        zoneFour()


# GLOTV
def gloTV():
    gTV = input(
        "1. Proceed (Auto-Renew)\n"
        "2. Proceed (One-off)\n"
        "0. Back\n"
    )
    if gTV == "1":
        gloAutorenew()
    elif gTV == "2":
        gloOneoff()
    elif gTV == "0":
        selectTrans()
    else:
        print("Wrong input")
        gloTV()


# gloAutorenew
def gloAutorenew():
    gAuto = input(
        "1. #150 = VOD 500MB 3Days\n"
        "2. #450 = VOD 2GB 7Days\n"
        "3. #1400 = VOD 6GB 30Days\n"
        "4. #900 = VOD+TV 2GB 7Days\n"
        "5. #3200 = VOD+TV 6GB 30Days\n"
        "6. Back\n"
        "7. Exit\n"
    )
    if gAuto == "1":
        print("You have been credited with #150, 500MB, VOD valid for 3 days")
    elif gAuto == "2":
        print("You have been credited with #450, 2GB, VOD valid for 7 days")
    elif gAuto == "3":
        print("You have been credited with #1400, 6GB, VOD valid for 30 days")
    elif gAuto == "4":
        print("You have been credited with #900, 2GB, VOD+TV valid for 7 days")
    elif gAuto == "5":
        print("You have been credited with #3200, 6GB, VOD+TV valid for 30 days")
    elif gAuto == "6":
        gloTV()
    elif gAuto == "7":
        print("Glo Unlimited")
    else:
        print("Wrong input, Please wait")
        gloAutorenew()


# gloOneoff
def gloOneoff():
    gOne = input(
        "1. #150 = VOD 500MB 3Days\n"
        "2. #450 = VOD 2GB 7Days\n"
        "3. #1400 = VOD 6GB 30Days\n"
        "4. #900 = VOD+TV 2GB 7Days\n"
        "5. #3200 = VOD+TV 6GB 30Days\n"
        "6. Back\n"
        "7. Exit\n"
    )
    if gOne == "1":
        print("You have been credited with #150, 500MB, VOD valid for 3 days")
    elif gOne == "2":
        print("You have been credited with #450, 2GB, VOD valid for 7 days")
    elif gOne == "3":
        print("You have been credited with #1400, 6GB, VOD valid for 30 days")
    elif gOne == "4":
        print("You have been credited with #900, 2GB, VOD+TV valid for 7 days")
    elif gOne == "5":
        print("You have been credited with #3200, 6GB, VOD+TV valid for 30 days")
    elif gOne == "6":
        gloTV()
    elif gOne == "7":
        print("Glo Unlimited")
    else:
        print("Wrong input, Please wait")
        gloOneoff()


# 11koboplan
def koboPlan():
    kPlan = input(
        "The most affordale 11k/sec Tariff Plan\n"
        "press\n"
        "1. To subscribe\n"
        "2. Back\n"
        "3. Exit\n"
        "Alternatively dial *311# to subscribe\n"
    )
    if kPlan == "1":
        print("You have subscribed to Glo's 11k/sec Tariff Plan")
    elif kPlan == "2":
        selectTrans()
    elif kPlan == "3":
        print('Glo Unlimited')
    else:
        print('Wrong code, try again')
        koboPlan()


# VAS
def vas():
    vasOptions = input(
        "1. Gamebox\n"
        "2. Glo Cloud\n"
        "3. Busuu Language learning\n"
        "4. Gaming Portal\n"
        "5. Caller Tunes\n"
        "6. Borrow Me Credit\n"
        "7. Unsubscribe\n"
        "8. Back\n"
        "0. Exit\n"
    )
    if vasOptions == "1":
        gameBox()
    elif vasOptions == "2":
        gloCloud()
    elif vasOptions == "3":
        busuuLL()
    elif vasOptions == "4":
        gamingPortal()
    elif vasOptions == "5":
        callerTunes()
    elif vasOptions == "6":
        borrowCreditOrData()
    elif vasOptions == "7":
        print("You have successfully unsubscribed from your VAS plan")
    elif vasOptions == "8":
        selectTrans()
    elif vasOptions == "0":
        print("Glo Unlimited")
    else:
        print("Wrong input, Please wait")
        vas()


# gamebox
def gameBox():
    gameb = input(
        "1. Weekly Auto Pack @ #55\n"
        "2. Monthly Auto Pack @ #155\n"
        "3. Weekly One-time Pack @ #55\n"
        "4. Monthly One-time Pack @ #155\n"
        "5. Back\n"
        "0. Exit\n"
    )
    if gameb == "1":
        print("You have subscribed to gamebox weekly auto pack")
    elif gameb == "2":
        print("You have subscribed to gamebox monthly auto pack")
    elif gameb == "3":
        print("You have subscribed to gamebox weekly one time pack")
    elif gameb == "4":
        print("You have subscribed to gamebox monthly one time pack")
    elif gameb == "5":
        vas()
    elif gameb == "0":
        print("Glo Unlimited")
    else:
        print("Wrong input")
        gameBox()


# Glocloud
def gloCloud():
    gcloud = input(
        "1st Month free, press\n"
        "1. Glo Cloud auto pack of 50GB @#250\n"
        "2. Glo Cloud one-time pack of 50GB @#250\n"
        "3. Back\n"
        "0. Exit\n"
    )
    if gcloud == "1":
        print("You have subscribed to Glo Cloud auto pack")
    elif gcloud == "2":
        print("You have subscribed to Glo Cloud one time pack")
    elif gcloud == "3":
        vas()
    elif gcloud == "0":
        print("Glo Unlimited")
    else:
        print("Wrong input")
        gloCloud()


# busuulearninglanguage
def busuuLL():
    bLL = input(
        "Subscribe Busuu Language learning. Press\n"
        "1. Busuu weekly auto pack @ 100\n"
        "2. Busuu weekly One time pack @ 100\n"
        "3. Daily auto pack @20\n"
        "4. Daily One time pack @20\n"
        "5. Back\n"
        "0. Exit\n"
    )
    if bLL == "1":
        print("You have subscribed to busuu weekly auto pack")
    elif bLL == "2":
        print("You have subscribed to busuu weekly one time pack")
    elif bLL == "3":
        print("You have subscribed to busuu daily auto pack")
    elif bLL == "4":
        print("You have subscribed to busuu daily one time pack")
    elif bLL == "5":
        vas()
    elif bLL == "0":
        print("Glo Unlimited")
    else:
        print("Wrong input")
        busuuLL()


# GamingPortal
def gamingPortal():
    gameport = input(
        "Subscribe below, on weekly pack for Gaming Portal.\n"
        "Press\n"
        "1. Daily auto pack @30\n"
        "2. Daily onetime pack @30\n"
        "3. Back\n"
        "0. Exit\n"
    )
    if gameport == "1":
        print("You have subscribed to gaming portal daily auto pack")
    elif gameport == "2":
        print("You have subscribed to gaming portal daily one time pack")
    elif gameport == "3":
        vas()
    elif gameport == "0":
        print("Glo Unlimited")
    else:
        print("Wrong input")
        gamingPortal()


# callerTunes
def callerTunes():
    cT = input(
        "Welcome to Caller tunes\n"
        "1. Hot 10\n"
        "2. New Tunes\n"
        "3. Professional Tunes\n"
        "4. Inspiration\n"
        "5. Bible Verses\n"
        "6. Album Tunes\n"
        "7. Others\n"
        "8. Unsubscribe\n"
    )
    if cT == "1":
        print("You have successfully activated Hot10 as your callertune")
    elif cT == "2":
        print("You have successfully activated New Tunes as your callertune")
    elif cT == "3":
        print("You have successfully activated Professional Tunes as your callertune")
    elif cT == "4":
        print("You have successfully activated Inspiration as your callertune")
    elif cT == "5":
        print("You have successfully activated Bible Verses as your callertune")
    elif cT == "6":
        print("You have successfully activated Album Tunes as your callertune")
    elif cT == "7":
        print("You have successfully activated Others as your callertune")
    elif cT == "8":
        print("You have successfully unsubscribed from callertunes")
    else:
        print("Wrong input")
        callerTunes()


# borrow me credit info
def BMCinfo():
    bMC = input(
        "Never be out of airtime or data. BMC allows you\n"
        "access even when you are out of cash. Dial any\n"
        "number to go back to menu\n"
        "0. Back\n"
    )
    if bMC == '0':
        borrowCreditOrData()
    else:
        borrowCreditOrData()


# borrow credit or data
def borrowCreditOrData():
    bCD = input(
        "Dear Customer, Welcome, you are eligible for #2000\n"
        "Reply with\n"
        "1. BMC info\n"
        "2. Borrow Credit\n"
        "3. Borrow Data\n"
        "4. Borrow Credit for Others\n"
        "5. Borrow Data for Others\n"
    )
    if bCD == "1":
        BMCinfo()
    elif bCD == "2":
        borrowCredit()
    elif bCD == "3":
        borrowData()
    elif bCD == "4":
        print("Dear Customer, your request stopped unexpectedly\n"
              "at this time. Please try again")
    elif bCD == "5":
        print("Dear Customer, your request stopped unexpectedly\n"
              "at this time. Please try again")
    else:
        print("Wrong input")
        borrowCreditOrData()


# borrow credit
def borrowCredit():
    bC = input(
        "You are eligible for #2000\n"
        "Reply with\n"
        "1. #25\n"
        "2. #50\n"
        "3. #100\n"
        "4. #200\n"
        "5. #500\n"
        "6. #1000\n"
        "7. #2000\n"
        "9. Balance\n"
        "0. Back\n"
    )
    if bC == "1":
        print("Your account has been successfully credited with #25")
    elif bC == "2":
        print("Your account has been successfully credited with #50")
    elif bC == "3":
        print("Your account has been successfully credited with #100")
    elif bC == "4":
        print("Your account has been successfully credited with #200")
    elif bC == "5":
        print("Your account has been successfully credited with #500")
    elif bC == "6":
        print("Your account has been successfully credited with #1000")
    elif bC == "7":
        print("Your account has been successfully credited with #2000")
    elif bC == "9":
        print("Your account balance is #0.64, Please recharge as soon as possible")
    elif bC == "0":
        borrowCreditOrData()
    else:
        print("Wrong input")
        borrowCredit()


# borrowData
def borrowData():
    bD = input(
        "You are eligible for #2000 worth of data.\n"
        "Reply with\n"
        "1. #50=35MB+5MB\n"
        "2. #100=95MB+35MB\n"
        "3. #200=200MB+110MB\n"
        "4. #500=650MB+550MB\n"
        "5. #1000=1.6GB+1GB\n"
        "6. #2000=4.4GB+600MB\n"
        "0. Back\n"
    )
    if bD == "1":
        print("Your account has been successfully credited with #50 worth of data")
    elif bD == "2":
        print("Your account has been successfully credited with #100 worth of data")
    elif bD == "3":
        print("Your account has been successfully credited with #200 worth of data")
    elif bD == "4":
        print("Your account has been successfully credited with #500 worth of data")
    elif bD == "5":
        print("Your account has been successfully credited with #1000 worth of data")
    elif bD == "6":
        print("Your account has been successfully credited with #2000 worth of data")
    elif bD == "0":
        borrowCreditOrData()
    else:
        print("Wrong input")
        borrowData()


def selectTrans():
    trans = input(
        "1. Festival Of Joy\n"
        "2. Data\n"
        "3. E-Topup\n"
        "4. Berekete 10X\n"
        "5. Tariff Plan\n"
        "6. Intl Calls & Roaming\n"
        "7. GLOTV\n"
        "8. 11KOBO Plan\n"
        "9. Borrow Credit or Data\n"
        "10. VAS\n"
    )
    if trans == "1":
        # Feast of joy
        feastJoy()
    elif trans == "2":
        # Buy Data
        data()
    elif trans == "3":
        # Buy e-top
        eTop()
    elif trans == "4":
        # Buy Berekete Plan
        berekete()
    elif trans == "5":
        # Tarrif plan
        tariffPlan()
    elif trans == "6":
        # IntlCall
        intCallsAndRoaming()
    elif trans == "7":
        # GLOTV
        gloTV()
    elif trans == "8":
        # 11KOBO Plan
        koboPlan()
    elif trans == "9":
        # Borrow Data and Airtime
        borrowCreditOrData()
    elif trans == "10":
        # VAS
        vas()
    else:
        print(
            "Invalid Transaction Entry\n"
            "Try Again"
        )
        selectTrans()


def ussd():
    usd = input("Enter USSD code: ")
    if usd == "*777#":
        print("Enter Transaction\n")
        selectTrans()

    else:
        print(
            "Invalid Transaction Entry\n"
            "Try Again"
        )
        ussd()


ussd()
