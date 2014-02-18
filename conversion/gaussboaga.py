#!/usr/bin/env python
import pyproj

    


def defintion_proj_gb2ll():
    import pyproj
    wgs84=pyproj.Proj(proj='latlong',datum='WGS84')
    gaussb = pyproj.Proj(init='epsg:26592',towgs84="-122.74,-34.27,-22.83,-1.884,-3.400,-3.030,-15.62")
    return gaussb,wgs84
    
def defintion_proj_ll2gb():
    import pyproj
    wgs84=pyproj.Proj(proj='latlong',datum='WGS84')
    gaussb = pyproj.Proj(init='epsg:26592',towgs84="-122.74,-34.27,-22.83,-1.884,-3.400,-3.030,-15.62")
    return wgs84,gaussb


def convert(data,from_coordinate,to_coordinate,utmzone=None):
    import pyproj
    x,y=pyproj.transform(from_coordinate,to_coordinate,data[0],data[1])
    if len(data) > 2:
        return x,y," ".join(str(x) for x in data[2:])
    else: 
        return x,y



if  __name__ == '__main__':
    
    try:
        import optparse_gui
    except:
        pass
        
    import optparse
    import sys
    import pyproj
    
    
    if 1 == len( sys.argv ):
            try:
                option_parser_class = optparse_gui.OptionParser
            except:
                option_parser_class = optparse.OptionParser
    else:
            option_parser_class = optparse.OptionParser
    
    
    usage = """
    
from point 2 point:
       
       usage: COORDINATES_CONVERSION.py [trasformation flag]  coord1 coord2 [....]
       
from file to file:
       
       usage: COORDINATES_CONVERSION.py --file filename [trasformation flag]
       
            filename: is a file in xyz format
            
from unix pipe:
    
        i.e. echo '12 43' | COORDINATES_CONVERSION.py  [trasformation flag]
            
traformation flag:
     
--ll2gb = from geographical coordinates to gauss boaga
--gb2ll = from gauss boaga to geographical coordinates
_____________________________

                            
The datum is WGS84
     
    """
    
    parser = option_parser_class(usage=usage)
    
    parser.add_option("--point",action="store_true", dest="point", default=False,help="set the option point2point true")
    parser.add_option("--file",dest="filename", default=False,help="name of the file")
    parser.add_option("--pipe",action="store_true",dest="pipe", default=True,help="unix pipe")
    
    parser.add_option("--ll2gb", action="store_true",dest="ll2gb", default=False,help="from geographical coordinates to gauss boaga")
    parser.add_option("--gb2ll", action="store_true",dest="gb2ll", default=False,help="from gauss boaga to geographical coordinates")

    
    (options, args) = parser.parse_args()
    #print options,args
    
    if options.ll2gb:
        from_coordinate,to_coordinate=defintion_proj_ll2gb()
    elif options.gb2ll:    
        from_coordinate,to_coordinate=defintion_proj_gb2ll()
    else:
        print 'no transformation flag'
        print 
        print parser.usage
        sys.exit()
    
    if len(args) != 0:
        record=map(float,args)
        dc=convert(record,from_coordinate,to_coordinate)
        print ' '.join(str(x) for x in dc)
    elif options.filename:
        f=open(options.filename,'r')
        data=f.readlines()
        for d in data:
            record=map(float,d.split())
            dc=convert(record,from_coordinate,to_coordinate)
            print ' '.join(str(x) for x in dc)
    elif options.pipe or options.uz: 
        data = sys.stdin.readlines()
        for r in data:
            record=map(float,r.split())
            dc=convert(record,from_coordinate,to_coordinate)
            print ' '.join(str(x) for x in dc)
    else:
        print 'no input'
        print parser.usage
        sys.exit()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    