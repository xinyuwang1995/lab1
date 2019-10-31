import hashids


def hashid(_id,length=6):
    KEY = 'wangxinyu'

    hasher = hashids.Hashids(salt=KEY,min_length=length)
    return hasher.encode(_id)



