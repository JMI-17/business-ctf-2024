FLAG = b'HTB{what_a_cool_random_number_generator_by_bluuuuuum_bluuuuuum_and_shuuuuuub_i_implemented_it_securely_didnt_i?}'

KEY = b'1_4m_y0ur_k3y_t0_g3t_th3_fl4g123'

MESSAGES = [
    'Welcome! If you see this you have successfully decrypted the first message. To get the symmetric key that decrypts the flag you need to do the following:\n\n1. Collect all 5 shares from these messages\n2. Use them to interpolate the polynomial in a finite field that will be revealed in another message\n3. Convert the constant term of the polynomial to bytes and use it to decrypt the flag. Here is your first share!\n\nShare#1#: ',

    'Keep up the good work! Offered say visited elderly and. Waited period are played family man formed. He ye body or made on pain part meet. You one delay nor begin our folly abode. By disposed replying mr me unpacked no. As moonlight of my resolving unwilling. Turned it up should no valley cousin he. Speaking numerous ask did horrible packages set. Ashamed herself has distant can studied mrs.\n\nShare#2#: ',

    'Only a few more are left! Of be talent me answer do relied. Mistress in on so laughing throwing endeavor occasion welcomed. Gravity sir brandon calling can. No years do widow house delay stand. Prospect six kindness use steepest new ask. High gone kind calm call as ever is. Introduced melancholy estimating motionless on up as do. Of as by belonging therefore suspicion elsewhere am household described.\n\nShare#3#: ',

    'You are almost there! Not him old music think his found enjoy merry. Listening acuteness dependent at or an. Apartments thoroughly unsatiable terminated sex how themselves. She are ten hours wrong walls stand early. Domestic perceive on an ladyship extended received do. Why jennings our whatever his learning gay perceive. Is against no he without subject. Bed connection unreserved preference partiality not unaffected.\n\nShare#4#: ',

    'Congratulations!!! Not him old music think his found enjoy merry. Listening acuteness dependent at or an. Apartments thoroughly unsatiable terminated how themselves. She are ten hours wrong walls stand early. Domestic perceive on an ladyship extended received do. You need to interpolate the polynomial in the finite field GF(%s).\n\nShare#5#: '
]