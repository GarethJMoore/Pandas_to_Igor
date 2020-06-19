def save_pd(df, name=None, as_ibw = False):
    #If you don't give a name it takes the name of the DataFrame passed
    if not name:
        name =[x for x in globals() if globals()[x] is df][0]
    
    #Converts data in DataFrame floats
    df = df.apply(pd.to_numeric, downcast='float', errors='coerce')
        
    #Opens a .itx file for writing in the current directory
    with open("./{0}.itx".format(name),'w') as fp:
        for column in df.columns:
            
            #Igor won't accept a wave called 'time'
            igor_wave_name = 'times' if 'time' in column else column
            
            #Converts each column to an np.array, then to an IgorWave5 (see package lit) then saves
            if as_ibw:
                exec("IgorWave5(np.asarray(df.{0}),'{1}_{2}').save('./{1}_{2}.ibw')".format(column,name,igor_wave_name))
            else:
                exec("IgorWave5(np.asarray(df.{0}),'{1}_{2}').save_itx(fp)".format(column,name,igor_wave_name))
