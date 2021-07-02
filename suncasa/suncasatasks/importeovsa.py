##################### generated by xml-casa (v2) from importeovsa.xml ###############
##################### 27a519e51ee300bf7df502106dade919 ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from .private.task_importeovsa import importeovsa as _importeovsa_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log

class _importeovsa:
    """
    importeovsa ---- Parallelized import EOVSA idb file(s) to a measurement set or multiple measurement set.

    
    Parallelized imports an arbitrary number of EOVSA idb-format data sets into
    a casa measurement set. If more than one band is present, they
    will be put in the same measurement set but in a separate spectral
    window.
    

    --------- parameter descriptions ---------------------------------------------

    idbfiles          Name of input EOVSA idb file(s) or observation time range.
    ncpu              Number of cpu cores to use
    timebin           Bin width for time averaging
    width             Width of output channel relative to MS channel (# to average)
    visprefix         Prefix of vis names (may include the path).
    udb_corr          if applying correction to input UDB files before import to MS.
    use_exist_udbcorr If use the existed udb_corr results.
    nocreatms         If setting nocreatms True, will simulate a model measurement set for the first idb file and copy the model for the rest of idl files in list. If False, will simulate a new measurement set for every idbfile in list.
    doconcat          If concatenate multi casa measurement sets to one file.
    modelms           Name of input model measurement set file. If modelms is assigned, no simulation will start.
    doscaling         If creating a new MS file with the amplitude of visibility data rescaled.
    keep_nsclms       Keep the no scaling measurement sets

    --------- examples -----------------------------------------------------------

    
    
    Parallelized imports an arbitrary number of EOVSA idb-format data sets into
    a casa measurement set. If more than one band is present, they
    will be put in the same measurement set but in a separate spectral
    window.
    
    Detailed Keyword arguments:
    
    idbfiles -- Name of input EOVSA idb file(s)
    default: none. Must be supplied
    example: idbfiles = 'IDB20160524000518'
    example: idbfiles=['IDB20160524000518','IDB20160524000528']
    
    ncpu -- Number of cpu cores to use
    default: 8
    
    visprefix -- Prefix of vis names (may include the path)
    default: none;
    example: visprefix='sun/']
    
    
    --- Data Selection ---
    
    nocreatms -- If copying a new MS file instead of create one from MS simulator.
    default: False
    
    modelms -- Name of the standard Measurement Set. IF modelms is not provided, use
    '/home/user/sjyu/20160531/ms/sun/SUN/SUN_20160531T142234-10m.1s.ms' as a standard MS.
    
    doconcat -- If outputing one single MS file
    
    
    --- Channel averaging parameter ---
    
    width -- Number of input channels to average to create an output
    channel. If a list is given, each bin will apply to one spw in
    the selection.
    default: 1 => no channel averaging.
    options: (int) or [int]
    
    example: chanbin=[2,3] => average 2 channels of 1st selected
    spectral window and 3 in the second one.
    
    
    --- Time averaging parameters ---
    
    timebin -- Bin width for time averaging. When timebin is greater than 0s,
    the task will average data in time. Flagged data will be included
    in the average calculation, unless the parameter keepflags is set to False.
    In this case only partially flagged rows will be used in the average.
    default: '0s'
    
    
    
    
    
    
    
    
    
    


    """

    _info_group_ = """Import/export"""
    _info_desc_ = """Parallelized import EOVSA idb file(s) to a measurement set or multiple measurement set."""

    def __call__( self, idbfiles='', ncpu=int(1), timebin='0s', width=int(1), visprefix='', udb_corr=True, use_exist_udbcorr=False, nocreatms=False, doconcat=False, modelms='', doscaling=False, keep_nsclms=False ):
        schema = {'idbfiles': {'anyof': [{'type': 'cStr', 'coerce': _coerce.to_str}, {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}]}, 'ncpu': {'type': 'cInt'}, 'timebin': {'type': 'cStr', 'coerce': _coerce.to_str}, 'width': {'anyof': [{'type': 'cStr', 'coerce': _coerce.to_str}, {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}, {'type': 'cInt'}, {'type': 'cIntVec', 'coerce': [_coerce.to_list,_coerce.to_intvec]}]}, 'visprefix': {'type': 'cStr', 'coerce': _coerce.to_str}, 'udb_corr': {'type': 'cBool'}, 'use_exist_udbcorr': {'type': 'cBool'}, 'nocreatms': {'type': 'cBool'}, 'doconcat': {'type': 'cBool'}, 'modelms': {'type': 'cStr', 'coerce': _coerce.to_str}, 'doscaling': {'type': 'cBool'}, 'keep_nsclms': {'type': 'cBool'}}
        doc = {'idbfiles': idbfiles, 'ncpu': ncpu, 'timebin': timebin, 'width': width, 'visprefix': visprefix, 'udb_corr': udb_corr, 'use_exist_udbcorr': use_exist_udbcorr, 'nocreatms': nocreatms, 'doconcat': doconcat, 'modelms': modelms, 'doscaling': doscaling, 'keep_nsclms': keep_nsclms}
        assert _pc.validate(doc,schema), str(_pc.errors)
        _logging_state_ = _start_log( 'importeovsa', [ 'idbfiles=' + repr(_pc.document['idbfiles']), 'ncpu=' + repr(_pc.document['ncpu']), 'timebin=' + repr(_pc.document['timebin']), 'width=' + repr(_pc.document['width']), 'visprefix=' + repr(_pc.document['visprefix']), 'udb_corr=' + repr(_pc.document['udb_corr']), 'use_exist_udbcorr=' + repr(_pc.document['use_exist_udbcorr']), 'nocreatms=' + repr(_pc.document['nocreatms']), 'doconcat=' + repr(_pc.document['doconcat']), 'modelms=' + repr(_pc.document['modelms']), 'doscaling=' + repr(_pc.document['doscaling']), 'keep_nsclms=' + repr(_pc.document['keep_nsclms']) ] )
        return _end_log( _logging_state_, 'importeovsa', _importeovsa_t( _pc.document['idbfiles'], _pc.document['ncpu'], _pc.document['timebin'], _pc.document['width'], _pc.document['visprefix'], _pc.document['udb_corr'], _pc.document['use_exist_udbcorr'], _pc.document['nocreatms'], _pc.document['doconcat'], _pc.document['modelms'], _pc.document['doscaling'], _pc.document['keep_nsclms'] ) )

importeovsa = _importeovsa( )
