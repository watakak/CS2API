offsets = {
    'dwLocalPlayerController': {
        'dwLocalPlayerController': 0x19A66C8,

        'fov': 0x6D4,  # m_iDesiredFOV, uint

        'ping': 0x720,  # m_iPing
        'alive': 0x7F4,  # m_bPawnIsAlive
        'health': 0x7F8,  # m_iPawnHealth
        'armor': 0x7FC,  # m_iPawnArmor
        'defuser': 0x800,  # m_bPawnHasDefuser
        'helmet': 0x801,  # m_bPawnHasHelmet
    },

    'dwLocalPlayerPawn': {
        'dwLocalPlayerPawn': 0x17C37F0,

        'walking': 0x2230,  # m_bIsWalking
        'scoped': 0x22A0,  # m_bIsScoped

        'in_buyzone': 0x14C8,  # m_bInBuyZone
        'in_bombzone': 0x1519,  # m_bInBombZone
        'in_rescuezone': 0x1518,  # m_bInHostageRescueZone
        'which_bombzone': 0x22B0,  # m_nWhichBombZone
        'not_in_defusearea': 0x22AC,  # m_bInNoDefuseArea

        'defusing': 0x22A2,  # m_bIsDefusing
        'rescuing': 0x22A3,  # m_bIsGrabbingHostage

        'left_hand': 0x2179,  # m_bLeftHanded

        'shots_fired': 0x22B4,  # m_iShotsFired

        'm_pClippingWeapon': {
            'm_pClippingWeapon': 0x12F0,  # C_CSWeaponBase

            'fire': 0x1630,  # m_ePlayerFireEvent

            'seq_idle': 0x1638,  # 0x1638

            'reloading': 0x1740,  # m_bInReload
            'firemode': 0x1700,  # m_weaponMode
            'silencer': 0x1749,  # m_bSilencerOn

            'fire_left': 0x163C,  # m_seqFirePrimary
            'fire_right': 0x1640,  # m_seqFireSecondary

            'weapon_owner_t': 0x1835,  # m_bWasOwnedByTerrorist
            'weapon_owner_ct': 0x1834,  # m_bWasOwnedByCT

            'crosshair_width': 0x16A8,  # m_flCrosshairDistance, float

            'test2': 0xC22
        },

        'm_pWeaponServices': {
            'm_pWeaponServices': 0x10F8,

            'current_weapons': 0x40,  # m_hMyWeapons
            'active_weapons': 0x58,  # m_hActiveWeapon
            'last_weapon': 0x5C,  # m_hLastWeapon
            'ammo': 0x60,  # m_iAmmo
        },

        'm_pMovementServices': {
            'm_pMovementServices': 0x1138,

            'ducking': 0x1EC,  # m_bDucking

            'max_speed': 0x198,  # m_flMaxspeed
            'max_fall_velocity': 0x1DC,  # m_flMaxFallVelocity

            'duck_amount': 0x22C,  # m_flDuckAmount, float
            'duck_speed': 0x230,  # m_flDuckSpeed, float
            'duck_overdrive': 0x234,  # m_bDuckOverride, bool
            'duck_desire': 0x235,  # m_bDesiresDuck, bool
            'duck_offset': 0x238,  # m_flDuckOffset, float
            'duck_time': 0x23C,  # m_nDuckTimeMsecs, int
            'duck-jump_time': 0x240,  # m_nDuckJumpTimeMsecs, int
        },

        'm_skybox3d': {
            'm_skybox3d': 0x11B8,

            'sky_scale': 0x8,  # scale

            'fog': {
                'fog': 0x20,

                'fog_enable': 0x64,  # enable, bool
            },
        },

        'team': 0x3C3,  # m_iTeamNum, int
        'on_ground': 0x3CC, # m_fFlags, int

        'viewmodel_x': 0x2180,  # m_flViewmodelOffsetX
        'viewmodel_y': 0x2184,  # m_flViewmodelOffsetY
        'viewmodel_z': 0x2188,  # m_flViewmodelOffsetZ
        'viewmodel_fov': 0x218C,  # m_flViewmodelFOV

        'current_equipment': 0x22D8,  # m_unCurrentEquipmentValue
    },

    'dwEntityList': {
        'dwEntityList': 0x1956A68,
    },

    'dwGlowManager': {
        'dwGlowManager': 0x19C5508,
    },

    'dwGameRules': {
        'dwGameRules': 0x19C54E8,

        'game_freeze': 0x40,  # m_bFreezePeriod, bool
        'game_warmup': 0x40,   # m_bWarmupPeriod, bool
        'game_restart': 0x74,  # m_bGameRestart, bool

        'map_have_bombsite': 0x95,  # m_bMapHasBombTarget, bool
        'map_have_rescuezone': 0x95,  # m_bMapHasRescueZone , bool
        'map_have_buyzone': 0x95,  # m_bMapHasBuyZone, bool

        'hostages_remaining': 0x90,  # m_iHostagesRemaining, bool

        'queue_matchmaking': 0x98,  # m_bIsQueuedMatchmaking, bool

        'server_paused': 0x4C,   # m_bServerPaused, bool
        'game_rounds': 0x84,  # m_totalRoundsPlayed, int
        'overtime': 0x8C,  # m_nOvertimePlaying, int

        'bomb_dropped': 0x9A4,  # m_bBombDropped, bool
        'bomb_planted': 0x9A5,  # m_bBombPlanted, bool

        'round_end_message': 0xEA0, # m_sRoundEndMessage, CUtlString
    },

    'dwGameEntitySystem': {
        'dwGameEntitySystem': 0x1A76178,

        'test': 0x1574
    },

    'global': {  # buttons

        'left_click': 0x17BC020,  # attack
        'right_click': 0x17CC0B0,  # attack2

        'jump': 0x17BC530,  # jump
        'ctrl': 0x17BC5C0,  # duck

        'use': 0x17CC4A0,  # use
        'zoom': 0x19D9C20,  # zoom
        'reload': 0x17CBF90,  # reload
        'inspect': 0x19D9CB0,  # lookatweapon

        'W': 0x17CC260,  # forward
        'S': 0x17CC2F0,  # back
        'D': 0x17CC410,  # right
        'A': 0x17CC380,  # left
    }
}
