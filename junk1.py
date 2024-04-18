from pprint import pprint

def list_in_list(b):
        outside_list = []
        for each in range(0,b):
            inside_list = []      
            '''
            response1 = client2.describe_instances(
                                InstanceIds=[
                                    df['instance-id'].values[each],
                                ],
                                )
            '''
            inside_list.append(each)
            inside_list.append(each+1)
            inside_list.append(each+2)
            '''
            inside_list.append(response1['Reservations'][0]['Instances'][0]['InstanceType'])    
            inside_list.append(response1['Reservations'][0]['Instances'][0]['PrivateIpAddress'])
            inside_list.append(response1['Reservations'][0]['Instances'][0]['RootDeviceType'])
            inside_list.append(response1['Reservations'][0]['Instances'][0]['State']['Name'])
            '''
            outside_list.append(inside_list)
        return outside_list

a = list_in_list(5)

pprint(a)