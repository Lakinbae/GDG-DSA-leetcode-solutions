def longestCommonPrefix(strs):

    prefix= strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
        
    return prefix

    # main part
    if __name__ == "__main__":
        strs= ["lakin","lake","laker"]
    result= longestCommonPrefix(strs)
    print(f"result is:{result}")