import redis
import os

def dump_fake_hm(r, nkeys, nvalues):
    batch_size = 2000
    print(f'... dumping {nkeys} fake keys, {nvalues} elements per key')
    for i in range(nkeys):
        name = f'map_{i}'
        print(f'... dumping map #{i}')
        for batch in range(int(nvalues/batch_size)):
            start = batch * batch_size + 1
            end = (batch+1) * batch_size
            print(f'...... dumping key range : {start} to {end}')
            r.hmset(name, {f'key_{k}': 3456 for k in range(start, end+1)})

    print(f'... [done]')

if __name__=='__main__':

    # tunnel from k8s
    redis_endpoint = 'localhost'
    redis_port = '6378'
    num_map = 9
    map_len = 4_200_000

    print('Running Elasticache fake data generator ...')
    print(f'... connecting to redis : {redis_endpoint}:{redis_port}')

    r = redis.Redis(host=redis_endpoint, port=redis_port, db=0)
    print('info keyspace: ', r.info('keyspace'))
    print('info memory:', r.info('memory'))
    print('dbsize: ', r.dbsize())

    # populate hm
    print('... populating key map')
    dump_fake_hm(r, num_map, map_len)