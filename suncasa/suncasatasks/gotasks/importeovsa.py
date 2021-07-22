##################### generated by xml-casa (v2) from importeovsa.xml ###############
##################### 27a519e51ee300bf7df502106dade919 ##############################
from __future__ import absolute_import
from casashell.private.stack_manip import find_local as __sf__
from casashell.private.stack_manip import find_frame as _find_frame
from casatools.typecheck import validator as _pc
from casatools.coercetype import coerce as _coerce
from suncasatasks import importeovsa as _importeovsa_t
from collections import OrderedDict
import numpy
import sys
import os

import shutil

def static_var(varname, value):
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate

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

    __schema = {'idbfiles': {'anyof': [{'type': 'cStr', 'coerce': _coerce.to_str}, {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}]}, 'ncpu': {'type': 'cInt'}, 'timebin': {'type': 'cStr', 'coerce': _coerce.to_str}, 'width': {'anyof': [{'type': 'cStr', 'coerce': _coerce.to_str}, {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}, {'type': 'cInt'}, {'type': 'cIntVec', 'coerce': [_coerce.to_list,_coerce.to_intvec]}]}, 'visprefix': {'type': 'cStr', 'coerce': _coerce.to_str}, 'udb_corr': {'type': 'cBool'}, 'use_exist_udbcorr': {'type': 'cBool'}, 'nocreatms': {'type': 'cBool'}, 'doconcat': {'type': 'cBool'}, 'modelms': {'type': 'cStr', 'coerce': _coerce.to_str}, 'doscaling': {'type': 'cBool'}, 'keep_nsclms': {'type': 'cBool'}}

    def __init__(self):
        self.__stdout = None
        self.__stderr = None
        self.__root_frame_ = None

    def __globals_(self):
        if self.__root_frame_ is None:
            self.__root_frame_ = _find_frame( )
            assert self.__root_frame_ is not None, "could not find CASAshell global frame"
        return self.__root_frame_

    def __to_string_(self,value):
        if type(value) is str:
            return "'%s'" % value
        else:
            return str(value)

    def __validate_(self,doc,schema):
        return _pc.validate(doc,schema)

    def __do_inp_output(self,param_prefix,description_str,formatting_chars):
        out = self.__stdout or sys.stdout
        description = description_str.split( )
        prefix_width = 23 + 14 + 4
        output = [ ]
        addon = ''
        first_addon = True
        while len(description) > 0:
            ## starting a new line.....................................................................
            if len(output) == 0:
                ## for first line add parameter information............................................
                if len(param_prefix)-formatting_chars > prefix_width - 1:
                    output.append(param_prefix)
                    continue
                addon = param_prefix + ' #'
                first_addon = True
                addon_formatting = formatting_chars
            else:
                ## for subsequent lines space over prefix width........................................
                addon = (' ' * prefix_width) + '#'
                first_addon = False
                addon_formatting = 0
            ## if first word of description puts us over the screen width, bail........................
            if len(addon + description[0]) - addon_formatting + 1 > self.term_width:
                ## if we're doing the first line make sure it's output.................................
                if first_addon: output.append(addon)
                break
            while len(description) > 0:
                ## if the next description word puts us over break for the next line...................
                if len(addon + description[0]) - addon_formatting + 1 > self.term_width: break
                addon = addon + ' ' + description[0]
                description.pop(0)
            output.append(addon)
        out.write('\n'.join(output) + '\n')

    #--------- return nonsubparam values ----------------------------------------------

    def __width_dflt( self, glb ):
        return int(1)

    def __width( self, glb ):
        if 'width' in glb: return glb['width']
        return int(1)

    def __idbfiles_dflt( self, glb ):
        return ''

    def __idbfiles( self, glb ):
        if 'idbfiles' in glb: return glb['idbfiles']
        return ''

    def __doscaling_dflt( self, glb ):
        return False

    def __doscaling( self, glb ):
        if 'doscaling' in glb: return glb['doscaling']
        return False

    def __ncpu_dflt( self, glb ):
        return int(1)

    def __ncpu( self, glb ):
        if 'ncpu' in glb: return glb['ncpu']
        return int(1)

    def __modelms_dflt( self, glb ):
        return ''

    def __modelms( self, glb ):
        if 'modelms' in glb: return glb['modelms']
        return ''

    def __visprefix_dflt( self, glb ):
        return ''

    def __visprefix( self, glb ):
        if 'visprefix' in glb: return glb['visprefix']
        return ''

    def __timebin_dflt( self, glb ):
        return '0s'

    def __timebin( self, glb ):
        if 'timebin' in glb: return glb['timebin']
        return '0s'

    def __udb_corr_dflt( self, glb ):
        return True

    def __udb_corr( self, glb ):
        if 'udb_corr' in glb: return glb['udb_corr']
        return True

    def __nocreatms_dflt( self, glb ):
        return False

    def __nocreatms( self, glb ):
        if 'nocreatms' in glb: return glb['nocreatms']
        return False

    def __doconcat_dflt( self, glb ):
        return False

    def __doconcat( self, glb ):
        if 'doconcat' in glb: return glb['doconcat']
        return False

    #--------- return non subparam/when values ---------------------------------------------
    def __use_exist_udbcorr( self, glb ):
        if 'use_exist_udbcorr' in glb: return glb['use_exist_udbcorr']
        return False

    #--------- return inp/go default --------------------------------------------------
    def __use_exist_udbcorr_dflt( self, glb ):
        if self.__udb_corr( glb ) == bool(True): return bool(False)
        return None
    def __keep_nsclms_dflt( self, glb ):
        if self.__doscaling( glb ) == bool(True): return bool(False)
        return None

    #--------- return subparam values -------------------------------------------------
    def __keep_nsclms( self, glb ):
        if 'keep_nsclms' in glb: return glb['keep_nsclms']
        dflt = self.__keep_nsclms_dflt( glb )
        if dflt is not None: return dflt
        return False

    #--------- subparam inp output ----------------------------------------------------
    def __idbfiles_inp(self):
        description = ''
        value = self.__idbfiles( self.__globals_( ) )
        (pre,post) = ('','') if self.__validate_({'idbfiles': value},{'idbfiles': self.__schema['idbfiles']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('idbfiles',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __ncpu_inp(self):
        description = ''
        value = self.__ncpu( self.__globals_( ) )
        (pre,post) = ('','') if self.__validate_({'ncpu': value},{'ncpu': self.__schema['ncpu']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('ncpu',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __timebin_inp(self):
        description = ''
        value = self.__timebin( self.__globals_( ) )
        (pre,post) = ('','') if self.__validate_({'timebin': value},{'timebin': self.__schema['timebin']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('timebin',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __width_inp(self):
        description = ''
        value = self.__width( self.__globals_( ) )
        (pre,post) = ('','') if self.__validate_({'width': value},{'width': self.__schema['width']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('width',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __visprefix_inp(self):
        description = ''
        value = self.__visprefix( self.__globals_( ) )
        (pre,post) = ('','') if self.__validate_({'visprefix': value},{'visprefix': self.__schema['visprefix']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('visprefix',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __udb_corr_inp(self):
        description = ''
        value = self.__udb_corr( self.__globals_( ) )
        (pre,post) = ('','') if self.__validate_({'udb_corr': value},{'udb_corr': self.__schema['udb_corr']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('\x1B[1m\x1B[47m%-14.14s =\x1B[0m %s%-23s%s' % ('udb_corr',pre,self.__to_string_(value),post),description,13+len(pre)+len(post))
    def __use_exist_udbcorr_inp(self):
        description = ''
        value = self.__use_exist_udbcorr( self.__globals_( ) )
        (pre,post) = ('','') if self.__validate_({'use_exist_udbcorr': value},{'use_exist_udbcorr': self.__schema['use_exist_udbcorr']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('use_exist_udbcorr',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __nocreatms_inp(self):
        description = ''
        value = self.__nocreatms( self.__globals_( ) )
        (pre,post) = ('','') if self.__validate_({'nocreatms': value},{'nocreatms': self.__schema['nocreatms']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('nocreatms',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __doconcat_inp(self):
        description = ''
        value = self.__doconcat( self.__globals_( ) )
        (pre,post) = ('','') if self.__validate_({'doconcat': value},{'doconcat': self.__schema['doconcat']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('doconcat',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __modelms_inp(self):
        description = ''
        value = self.__modelms( self.__globals_( ) )
        (pre,post) = ('','') if self.__validate_({'modelms': value},{'modelms': self.__schema['modelms']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('modelms',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __doscaling_inp(self):
        description = ''
        value = self.__doscaling( self.__globals_( ) )
        (pre,post) = ('','') if self.__validate_({'doscaling': value},{'doscaling': self.__schema['doscaling']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('\x1B[1m\x1B[47m%-14.14s =\x1B[0m %s%-23s%s' % ('doscaling',pre,self.__to_string_(value),post),description,13+len(pre)+len(post))
    def __keep_nsclms_inp(self):
        if self.__keep_nsclms_dflt( self.__globals_( ) ) is not None:
             description = ''
             value = self.__keep_nsclms( self.__globals_( ) )
             (pre,post) = ('','') if self.__validate_({'keep_nsclms': value},{'keep_nsclms': self.__schema['keep_nsclms']}) else ('\x1B[91m','\x1B[0m')
             self.__do_inp_output('   \x1B[92m%-11.11s =\x1B[0m %s%-23s%s' % ('keep_nsclms',pre,self.__to_string_(value),post),description,9+len(pre)+len(post))

    #--------- global default implementation-------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def set_global_defaults(self):
        self.set_global_defaults.state['last'] = self
        glb = self.__globals_( )
        if 'doscaling' in glb: del glb['doscaling']
        if 'use_exist_udbcorr' in glb: del glb['use_exist_udbcorr']
        if 'idbfiles' in glb: del glb['idbfiles']
        if 'nocreatms' in glb: del glb['nocreatms']
        if 'timebin' in glb: del glb['timebin']
        if 'modelms' in glb: del glb['modelms']
        if 'visprefix' in glb: del glb['visprefix']
        if 'doconcat' in glb: del glb['doconcat']
        if 'ncpu' in glb: del glb['ncpu']
        if 'udb_corr' in glb: del glb['udb_corr']
        if 'keep_nsclms' in glb: del glb['keep_nsclms']
        if 'width' in glb: del glb['width']


    #--------- inp function -----------------------------------------------------------
    def inp(self):
        print("# importeovsa -- %s" % self._info_desc_)
        self.term_width, self.term_height = shutil.get_terminal_size(fallback=(80, 24))
        self.__idbfiles_inp( )
        self.__ncpu_inp( )
        self.__timebin_inp( )
        self.__width_inp( )
        self.__visprefix_inp( )
        self.__udb_corr_inp( )
        self.__use_exist_udbcorr_inp( )
        self.__nocreatms_inp( )
        self.__doconcat_inp( )
        self.__modelms_inp( )
        self.__doscaling_inp( )
        self.__keep_nsclms_inp( )

    #--------- tget function ----------------------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def tget(self,file=None):
        from casashell.private.stack_manip import find_frame
        from runpy import run_path
        filename = None
        if file is None:
            if os.path.isfile("importeovsa.last"):
                filename = "importeovsa.last"
        elif isinstance(file, str):
            if os.path.isfile(file):
                filename = file
        if filename is not None:
            glob = find_frame( )
            newglob = run_path( filename, init_globals={ } )
            for i in newglob:
                glob[i] = newglob[i]
            self.tget.state['last'] = self
        else:
            print("could not find last file, setting defaults instead...")
            self.set_global_defaults( )

    def __call__( self, idbfiles=None, ncpu=None, timebin=None, width=None, visprefix=None, udb_corr=None, use_exist_udbcorr=None, nocreatms=None, doconcat=None, modelms=None, doscaling=None, keep_nsclms=None ):
        def noobj(s):
           if s.startswith('<') and s.endswith('>'):
               return "None"
           else:
               return s
        _prefile = os.path.realpath('importeovsa.pre')
        _postfile = os.path.realpath('importeovsa.last')
        _return_result_ = None
        _arguments = [idbfiles,ncpu,timebin,width,visprefix,udb_corr,use_exist_udbcorr,nocreatms,doconcat,modelms,doscaling,keep_nsclms]
        _invocation_parameters = OrderedDict( )
        if any(map(lambda x: x is not None,_arguments)):
            # invoke python style
            # set the non sub-parameters that are not None
            local_global = { }
            if idbfiles is not None: local_global['idbfiles'] = idbfiles
            if ncpu is not None: local_global['ncpu'] = ncpu
            if timebin is not None: local_global['timebin'] = timebin
            if width is not None: local_global['width'] = width
            if visprefix is not None: local_global['visprefix'] = visprefix
            if udb_corr is not None: local_global['udb_corr'] = udb_corr
            if use_exist_udbcorr is not None: local_global['use_exist_udbcorr'] = use_exist_udbcorr
            if nocreatms is not None: local_global['nocreatms'] = nocreatms
            if doconcat is not None: local_global['doconcat'] = doconcat
            if modelms is not None: local_global['modelms'] = modelms
            if doscaling is not None: local_global['doscaling'] = doscaling

            # the invocation parameters for the non-subparameters can now be set - this picks up those defaults
            _invocation_parameters['idbfiles'] = self.__idbfiles( local_global )
            _invocation_parameters['ncpu'] = self.__ncpu( local_global )
            _invocation_parameters['timebin'] = self.__timebin( local_global )
            _invocation_parameters['width'] = self.__width( local_global )
            _invocation_parameters['visprefix'] = self.__visprefix( local_global )
            _invocation_parameters['udb_corr'] = self.__udb_corr( local_global )
            _invocation_parameters['use_exist_udbcorr'] = self.__use_exist_udbcorr( local_global )
            _invocation_parameters['nocreatms'] = self.__nocreatms( local_global )
            _invocation_parameters['doconcat'] = self.__doconcat( local_global )
            _invocation_parameters['modelms'] = self.__modelms( local_global )
            _invocation_parameters['doscaling'] = self.__doscaling( local_global )

            # the sub-parameters can then be set. Use the supplied value if not None, else the function, which gets the appropriate default
            _invocation_parameters['keep_nsclms'] = self.__keep_nsclms( _invocation_parameters ) if keep_nsclms is None else keep_nsclms

        else:
            # invoke with inp/go semantics
            _invocation_parameters['idbfiles'] = self.__idbfiles( self.__globals_( ) )
            _invocation_parameters['ncpu'] = self.__ncpu( self.__globals_( ) )
            _invocation_parameters['timebin'] = self.__timebin( self.__globals_( ) )
            _invocation_parameters['width'] = self.__width( self.__globals_( ) )
            _invocation_parameters['visprefix'] = self.__visprefix( self.__globals_( ) )
            _invocation_parameters['udb_corr'] = self.__udb_corr( self.__globals_( ) )
            _invocation_parameters['use_exist_udbcorr'] = self.__use_exist_udbcorr( self.__globals_( ) )
            _invocation_parameters['nocreatms'] = self.__nocreatms( self.__globals_( ) )
            _invocation_parameters['doconcat'] = self.__doconcat( self.__globals_( ) )
            _invocation_parameters['modelms'] = self.__modelms( self.__globals_( ) )
            _invocation_parameters['doscaling'] = self.__doscaling( self.__globals_( ) )
            _invocation_parameters['keep_nsclms'] = self.__keep_nsclms( self.__globals_( ) )
        try:
            with open(_prefile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-11s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#importeovsa( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: pass
        try:
            _return_result_ = _importeovsa_t( _invocation_parameters['idbfiles'],_invocation_parameters['ncpu'],_invocation_parameters['timebin'],_invocation_parameters['width'],_invocation_parameters['visprefix'],_invocation_parameters['udb_corr'],_invocation_parameters['use_exist_udbcorr'],_invocation_parameters['nocreatms'],_invocation_parameters['doconcat'],_invocation_parameters['modelms'],_invocation_parameters['doscaling'],_invocation_parameters['keep_nsclms'] )
        except Exception as e:
            from traceback import format_exc
            from casatasks import casalog
            casalog.origin('importeovsa')
            casalog.post("Exception Reported: Error in importeovsa: %s" % str(e),'SEVERE')
            casalog.post(format_exc( ))
            _return_result_ = False
        try:
            os.rename(_prefile,_postfile)
        except: pass
        return _return_result_

importeovsa = _importeovsa( )

