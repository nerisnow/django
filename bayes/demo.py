def testfunc(request):
    with open(TEST_SRC, 'r') as file:
        test = list(csv.reader(file))
        d = []
        #d={}
    for r in test:
        prediction = [make_decision(r[0], make_class_prediction)]
        if (prediction == [1]):
            d.append(r[0])
            #d['data']= {"review": r[0]}
        #djson = json.dumps(d)
        print(d)
    #return JsonResponse(d,safe=False)
    return JsonResponse(d,safe=False)