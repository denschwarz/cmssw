import FWCore.ParameterSet.Config as cms

from ..modules.hltEgammaCandidatesUnseeded_cfi import *
from ..modules.hltEgammaClusterShapeUnseeded_cfi import *
from ..modules.hltEgammaEcalPFClusterIsoUnseeded_cfi import *
from ..modules.hltEgammaEleGsfTrackIsoV6Unseeded_cfi import *
from ..modules.hltEgammaEleL1TrkIsoUnseeded_cfi import *
from ..modules.hltEgammaHcalPFClusterIsoUnseeded_cfi import *
from ..modules.hltEgammaHGCALIDVarsUnseeded_cfi import *
from ..modules.hltEgammaHGCalLayerClusterIsoUnseeded_cfi import *
from ..modules.hltEgammaHoverEUnseeded_cfi import *

HLTEle32WPTightUnseededInnerSequence = cms.Sequence(hltEgammaHGCALIDVarsUnseeded+hltEgammaEcalPFClusterIsoUnseeded+hltEgammaHGCalLayerClusterIsoUnseeded+hltEgammaHcalPFClusterIsoUnseeded+hltEgammaCandidatesUnseeded+hltEgammaClusterShapeUnseeded+hltEgammaEleGsfTrackIsoV6Unseeded+hltEgammaEleL1TrkIsoUnseeded+hltEgammaHoverEUnseeded)
