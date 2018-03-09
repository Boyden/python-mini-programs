# block.py

import hashlib
import uuid


class Block(object):
    def __init__(self, data=None, previous_hash=None):
        self.identifier = uuid.uuid4().hex   # 产生唯一标示
        self.nonce = None                    # nonce值
        self.data = data                     # 区块内容
        self.previous_hash = previous_hash   # 父节点哈希值
        
    def hash(self, nonce=None):
        '''
        计算区块的哈希值
        '''
        message = hashlib.sha256()
        message.update(self.identifier.encode('utf-8'))
        message.update(str(nonce).encode('utf-8'))
        message.update(str(self.data).encode('utf-8'))
        message.update(str(self.previous_hash).encode('utf-8'))

        return message.hexdigest()

    def hash_is_valid(self, the_hash):
        '''
        校验区块哈希值有否有效
        '''
        return the_hash.startswith('19980116')

    def __repr__(self):
        return 'Block<Hash: {}, Nonce: {}>'.format(self.hash(self.nonce), self.nonce)
    
    
    '''
        新增挖矿函数
    '''
    def mine(self):
        # 初始化nonce为0
        cur_nonce = self.nonce or 0

        # 循环直到生成一个有效的哈希值
        while True:
            the_hash = self.hash(nonce=cur_nonce)
            if self.hash_is_valid(the_hash):   # 如果生成的哈希值有效
                self.nonce = cur_nonce         # 保持当前nonce值
                break                          # 并退出
            else:
                cur_nonce += 1   # 若当前哈希值无效，更新nonce值，进行加1操作

class BlockChain(object):
    def __init__(self):
        self.head = None   # 指向最新的一个区块
        self.blocks = {}   # 包含所有区块的一个字典

    '''
        添加区块函数
    '''
    def add_block(self, new_block):
        previous_hash = self.head.hash(self.head.nonce) if self.head else None
        new_block.previous_hash = previous_hash

        self.blocks[new_block.identifier] = {
            'block': new_block,
            'previous_hash': previous_hash,
            'previous': self.head,
        }
        self.head = new_block

    def __repr__(self):
        num_existing_blocks = len(self.blocks)
        return 'Blockchain<{} Blocks, Head: {}>'.format(
            num_existing_blocks,
            self.head.identifier if self.head else None
        )