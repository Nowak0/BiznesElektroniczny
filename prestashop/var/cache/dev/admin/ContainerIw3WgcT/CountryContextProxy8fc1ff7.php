<?php

namespace ContainerIw3WgcT;

class CountryContextProxy8fc1ff7 extends \PrestaShop\PrestaShop\Core\Context\CountryContext implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyProxyTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".'*'."\0".'callPrefix' => [parent::class, 'callPrefix', null, 8],
        "\0".'*'."\0".'containsStates' => [parent::class, 'containsStates', null, 8],
        "\0".'*'."\0".'currencyId' => [parent::class, 'currencyId', null, 8],
        "\0".'*'."\0".'id' => [parent::class, 'id', null, 8],
        "\0".'*'."\0".'identificationNumberNeeded' => [parent::class, 'identificationNumberNeeded', null, 8],
        "\0".'*'."\0".'isoCode' => [parent::class, 'isoCode', null, 8],
        "\0".'*'."\0".'name' => [parent::class, 'name', null, 8],
        "\0".'*'."\0".'taxLabelDisplayed' => [parent::class, 'taxLabelDisplayed', null, 8],
        "\0".'*'."\0".'zipCodeFormat' => [parent::class, 'zipCodeFormat', null, 8],
        "\0".'*'."\0".'zipCodeNeeded' => [parent::class, 'zipCodeNeeded', null, 8],
        "\0".'*'."\0".'zoneId' => [parent::class, 'zoneId', null, 8],
        'callPrefix' => [parent::class, 'callPrefix', null, 8],
        'containsStates' => [parent::class, 'containsStates', null, 8],
        'currencyId' => [parent::class, 'currencyId', null, 8],
        'id' => [parent::class, 'id', null, 8],
        'identificationNumberNeeded' => [parent::class, 'identificationNumberNeeded', null, 8],
        'isoCode' => [parent::class, 'isoCode', null, 8],
        'name' => [parent::class, 'name', null, 8],
        'taxLabelDisplayed' => [parent::class, 'taxLabelDisplayed', null, 8],
        'zipCodeFormat' => [parent::class, 'zipCodeFormat', null, 8],
        'zipCodeNeeded' => [parent::class, 'zipCodeNeeded', null, 8],
        'zoneId' => [parent::class, 'zoneId', null, 8],
    ];

    public function getId(): int
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getId(...\func_get_args());
        }

        return parent::getId(...\func_get_args());
    }

    public function getZoneId(): int
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getZoneId(...\func_get_args());
        }

        return parent::getZoneId(...\func_get_args());
    }

    public function getCurrencyId(): int
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getCurrencyId(...\func_get_args());
        }

        return parent::getCurrencyId(...\func_get_args());
    }

    public function getIsoCode(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getIsoCode(...\func_get_args());
        }

        return parent::getIsoCode(...\func_get_args());
    }

    public function getCallPrefix(): int
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getCallPrefix(...\func_get_args());
        }

        return parent::getCallPrefix(...\func_get_args());
    }

    public function getName(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getName(...\func_get_args());
        }

        return parent::getName(...\func_get_args());
    }

    public function containsStates(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->containsStates(...\func_get_args());
        }

        return parent::containsStates(...\func_get_args());
    }

    public function isIdentificationNumberNeeded(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isIdentificationNumberNeeded(...\func_get_args());
        }

        return parent::isIdentificationNumberNeeded(...\func_get_args());
    }

    public function isZipCodeNeeded(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isZipCodeNeeded(...\func_get_args());
        }

        return parent::isZipCodeNeeded(...\func_get_args());
    }

    public function getZipCodeFormat(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getZipCodeFormat(...\func_get_args());
        }

        return parent::getZipCodeFormat(...\func_get_args());
    }

    public function isTaxLabelDisplayed(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isTaxLabelDisplayed(...\func_get_args());
        }

        return parent::isTaxLabelDisplayed(...\func_get_args());
    }
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('CountryContextProxy8fc1ff7', false)) {
    \class_alias(__NAMESPACE__.'\\CountryContextProxy8fc1ff7', 'CountryContextProxy8fc1ff7', false);
}
