Retrieves point data from the STVL database in :class:`Geopoints` or :class:`Geopointset` formats. The output format depends on the retrieval options. The generic rule is that STVL generates one :class:`Geopoints` object per date, time and step. When STVL generates a single :class:`Geopoints` this is returned as is. However, when multiple :class:`Geopoints` objects are generated they are merged into a single :class:`Geopointset` on return. The following examples show how it works.

This code retrieves a **single** date and time: 

    .. code-block:: python

        import metview as mv

        r = mv.stvl(
            parameter="2t",
            dates=20200511,
            times=12
        )
        
        print(f"type={type(r)}")
        print(f"len={len(r)}")   

generating this output::

        type=<class 'metview.bindings.Geopoints'>
        len=8474

This code retrieves **multiple** times:

    .. code-block:: python

        import metview as mv

        r = mv.stvl(
            parameter="2t",
            dates=20200511,
            times=[0, 12]
        )
        
        print(f"type={type(r)}")
        print(f"len={len(r)}")   
        for i, g in enumerate(r):
            print(f"len[{i}]={len(g)}")   
    

and the output looks like this::

    type=<class 'metview.bindings.GeopointSet'>
    len=2
    len[0]=7792
    len[1]=8474
      
 
