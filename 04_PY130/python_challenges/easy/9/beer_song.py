class BeerSong:  
    @classmethod
    def verse(cls, bottles):
        return cls.produce_text(bottles)
    
    @classmethod
    def verses(cls, start, stop):
        text = ""
        for n in range(start, stop - 1, -1):
            text += f"\n{cls.produce_text(n)}" if text else cls.produce_text(n)
        
        return text
    
    @classmethod
    def lyrics(cls):
        return cls.verses(99, 0)

    @classmethod
    def produce_text(cls, bottles):
        if bottles > 1:
            return (f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.\n"
                    f"Take one down and pass it around, {bottles - 1} {'bottles' if  bottles > 2 else 'bottle'} of beer on the wall.\n")
        elif bottles == 1:
            return (f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.\n"
                    f"Take it down and pass it around, no more bottles of beer on the wall.\n")
        else:
            return (f"No more bottles of beer on the wall, no more bottles of beer.\n"
                    f"Go to the store and buy some more, 99 bottles of beer on the wall.\n")